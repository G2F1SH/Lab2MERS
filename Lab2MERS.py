from PIL import Image
import argparse
import os


def convert_labpbr_to_mers(input_path, output_path, format='png'):
    """
    将LabPBR格式转换为MERS格式
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
                    
                    #排除alpha为0和255的情况，其他情况直接赋值
                    if a == 0:
                        new_g = 0
                    elif a == 255:
                        new_g = 0
                    else:
                        new_g = a

                    new_b = 255 - r  
                    
                    # B通道的65-255区间均匀映射到alpha的0-255，低于64映射为0
                    if b >= 65:
                        # 线性映射：(b-65)/(255-65) * 255
                        new_a = int((b - 65) / (255 - 65) * 255)
                    else:
                        new_a = 0
                    
                    new_img.putpixel((x, y), (new_r, new_g, new_b, new_a))
            
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
    
    args = parser.parse_args()
    
    if not os.path.exists(args.input):
        print(f"error: input file not found - {args.input}")
        return
    
    output_dir = os.path.dirname(args.output)
    if output_dir and not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    convert_labpbr_to_mers(args.input, args.output, args.format)


if __name__ == "__main__":
    main()
