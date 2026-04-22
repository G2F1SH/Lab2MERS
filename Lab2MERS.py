from PIL import Image
import argparse
import os


def convert_labpbr_to_mers(input_path, output_path, format='png', sss=False):
    """
    Convert LabPBR format to Bedrock MERS format
    """
    try:
        with Image.open(input_path) as img:
            if img.mode != 'RGBA':
                img = img.convert('RGBA')
            
            width, height = img.size
            
            new_img = Image.new('RGBA', (width, height))
            
            for x in range(width):
                for y in range(height):
                    r, g, b, a = img.getpixel((x, y))
                    
                    new_r = g 
                    
                    # Exclude cases where Alpha is 0 or 255; directly assign values for all other cases.
                    # 排除Alpha为0和255的情况，其他情况直接赋值
                    if a == 0:
                        new_g = 0
                    elif a == 255:
                        new_g = 0
                    else:
                        new_g = a

                    new_b = 255 - r  
                    
                    # Map the B channel range 65-255 linearly to alpha 0-255; values below 64 map to 0.
                    # B通道的65-255区间均匀映射到alpha的0-255，低于64映射为0
                    if b >= 65:
                        # Map the B channel range 65-255 linearly to alpha 0-255.
                        # 线性映射：(b-65)/(255-65) * 255
                        new_a = int((b - 65) / (255 - 65) * 255)
                    else:
                        new_a = 0
                    # When sss option is enabled and subsurface scattering is present, set metallic to 0.
                    # sss选项启用时且MERS中存在次表面散射，则将金属度置0
                    if sss and new_a > 0:
                        new_r = 0
                        
                    new_img.putpixel((x, y), (new_r, new_g, new_b, new_a))
            
            # Save the image in the specified format.
            # 根据指定格式保存
            new_img.save(output_path, format=format.upper())
            print(f"convert success：{input_path} → {output_path} (format: {format})")
            
    except Exception as e:
        print(f"convert failed：{str(e)}")


def main():
    parser = argparse.ArgumentParser(description='LabPBR-->MERS')
    parser.add_argument('input', help='input image path')
    parser.add_argument('output', help='output image path')
    parser.add_argument('--format', choices=['png', 'tga'], default='png', help='output format (default: png)')
    parser.add_argument('--sss', action='store_true', help='set metallic to 0 when subsurface scattering is present')
    
    args = parser.parse_args()
    
    if not os.path.exists(args.input):
        print(f"error: input file not found - {args.input}")
        return
    
    output_dir = os.path.dirname(args.output)
    if output_dir and not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    convert_labpbr_to_mers(args.input, args.output, args.format, args.sss)


if __name__ == "__main__":
    main()
