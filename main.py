print("Welcome to the Lazy Listers!")
print("This tool will help you generate product information for your e-commerce store.")
print("Please select the product category from the following options:")
print("1. Processor 2. CPU Cooler 3. Motherboard 4. Graphics Card")
print("5. RAM 6. Storage 7. Power Supply 8. Cabinet ")
print("9. Monitor 10. Keyboard 11. Mouse 12. Mouse Pad ")
print("13. Headset 14. Speaker 15. Thermal Paste 16. Cables ")
print("17. Laptop 18. Mini PC")

input_category=input("Enter the product category: ")

if input_category == "1" or input_category.lower() == "processor":
    product_category="Processor"
    print(f"You have selected {product_category}. Your Category is not available for this tool.")
    print("reach out to contact@sagarsardar.in for more information.")
elif input_category == "2" or input_category.lower() == "cpu cooler":
    product_category="CPU Cooler"
    print(f"You have selected {product_category}. Your Category is not available for this tool.")
    print("reach out to contact@sagarsardar.in for more information.")
elif input_category.lower() == "motherboard" or input_category.lower() == "3":
    product_category="Motherboard"
    print(f"You have selected {product_category}. Please provide the following details:")
    print("Enter the Motherboard Platform 1. AMD 2.Intel):")
    input_platform=input("Enter the Motherboard Platform:")
    if input_platform == "1" or input_platform.lower() == "amd":
        motherboard_platform="AMD"
    elif input_platform == "2" or input_platform.lower() == "intel":
        motherboard_platform="Intel"
    product_brand=input("Enter the Brand name(Ex: MSI):")
    product_model=input("Enter the Product Model(Ex: MAG B450M):")
    motherboard_chipset=input("Enter the Motherboard Chipset(Ex: B450):")
    motherboard_size=input("Enter the Motherboard Size(Ex: ATX):")
    cpu_socket=input("Enter the CPU Socket(Ex: AM4):")
    supported_processor=input("Enter the Supported Processor(Ex: AMD Ryzen):")
    print("Select the Supported Ram Type:")
    print("1. DDR4 2. DDR5")
    input_ram_type=input("Enter the Supported Ram Type:")
    if input_ram_type == "1" or input_ram_type.lower() == "ddr4":
        supported_ram_type="DDR4"
        custom_attribute_ram_type="DDR 4"
    elif input_ram_type == "2" or input_ram_type.lower() == "ddr5":
        supported_ram_type="DDR5"
        custom_attribute_ram_type="DDR 5"
    max_memory_support=input("Max Memory Support(Ex: 64):")
    max_memory_slots=input("Max Memory Slots(Ex: 4):")
    max_memory_speed=input("Max Memory Speed(Ex: 3200):")
    supported_pcie_slot=input("Supported PCIe Slot Version(Ex: 3.0):")
    motherboard_selling_price=int(input("Enter the Selling price of the motherboard:"))
    if motherboard_selling_price <= 10000:
        custom_attribute_motherboard_wattage="60W"
    elif motherboard_selling_price <= 20000:
        custom_attribute_motherboard_wattage="80W"
    else:
        custom_attribute_motherboard_wattage="100W"
    print("Select the Supported Ram Channel Type:")
    print("1. Single Channel 2. Dual Channel")
    input_ram_channel_type=input("Enter the Supported Ram Channel Type:")
    if input_ram_channel_type == "1" or input_ram_channel_type.lower().replace(" ","") =="singlechannel":
        motherboard_ram_channel_type="Single Channel"
    elif input_ram_channel_type == "2" or input_ram_channel_type.lower().replace(" ","") =="dualchannel":
        motherboard_ram_channel_type="Dual Channel"


    product_Name=(product_brand+" "+product_category+" "+" "+product_model+", "+motherboard_size+", "+cpu_socket+", "+supported_processor+", "+supported_ram_type+" Ram")
    h1_tag= (product_brand+" "+product_model+" "+motherboard_size+" "+supported_ram_type+" "+product_category)
    meta_tag_tittle=(product_brand+" "+product_model+" "+motherboard_size+" "+supported_ram_type+" "+product_category)
    meta_tag_description=(product_brand+" "+product_model+" | "+motherboard_size+" "+product_category+" | Supports "+supported_processor+" Processors, "+cpu_socket+" | Max "+ max_memory_support+"GB "+supported_ram_type+" "+max_memory_speed+"Mhz Memory | PCIe "+supported_pcie_slot+" Slot")
    product_sku=(product_brand+"-"+product_model).upper().replace(" ","-")
    seo_url=(product_brand+"-"+product_model+"-"+product_category).lower().replace(" ","-")
    

    with open("output.txt", "w") as f:
        f.write("Product Name: " + product_Name + "\n")
        f.write("H1 Tag: " + h1_tag + "\n")
        f.write("Meta Tag Title: " + meta_tag_tittle + "\n")
        f.write("Meta Tag Description: " + meta_tag_description + "\n")
        f.write("SKU: "+product_sku+"\n")
        f.write("SEO URL: " + seo_url + "\n")
        f.write("Product Sheet: "+ "\n")
        f.write("" + "\t" +product_Name+"\t"+product_model+ "\t"+product_sku+"\t"+""+"\t"+meta_tag_description+"\n")
        f.write("Attribute Sheet: "+ "\n")
        f.write("Motherboard  >  Platform "+"\t"+motherboard_platform + "\n")
        f.write("Motherboard  >  Socket "+"\t"+cpu_socket + "\n")
        f.write("Motherboard  >  Cpu Type "+"\t"+supported_processor + "\n")
        f.write("Motherboard  >  Chipset "+"\t"+motherboard_chipset + "\n")
        f.write("Motherboard  >  Memory Slots "+"\t"+max_memory_slots + "\n")
        f.write("Motherboard  >  Memory Speed "+"\t"+max_memory_speed + "\n")
        f.write("Motherboard  >  Max Memory Support "+"\t"+max_memory_support + "\n")
        f.write("Motherboard  >  Supported Memory Type "+"\t"+supported_ram_type + "\n")
        f.write("Motherboard  >  Channel Supported "+"\t"+motherboard_ram_channel_type + "\n")
        f.write("Motherboard  >  Memory Feature "+"\t"+"" + "\n")
        f.write("Motherboard  >  Graphics Port "+"\t"+"" + "\n")
        f.write("Motherboard  >  Expansion Slots "+"\t"+"" + "\n")
        f.write("Motherboard  >  Storage "+"\t"+"" + "\n")
        f.write("Motherboard  >  Wireless Networking "+"\t"+"" + "\n")
        f.write("Motherboard  >  Back Panel I/O Ports "+"\t"+"" + "\n")
        f.write("Motherboard  >  Internal I/O Connector "+"\t"+ "" + "\n")
        f.write("Motherboard  >  Form Factor "+"\t"+motherboard_size + "\n")
        f.write("Motherboard  >  Warranty "+"\t"+ "3 Years" + "\n")
        f.write("Motherboard  >  Note "+"\t"+ "" + "\n")
        f.write("CUSTOM CATEGORY ATTRIBUTE  >  Supported Motherboard Chipset - 468 (Custom Category) "+"\t"+motherboard_chipset + "\n")
        f.write("CUSTOM CATEGORY ATTRIBUTE  >  Supported Ram Motherboard Wise - 467 (Custom Category) "+"\t"+"" + "\n")
        f.write("CUSTOM CATEGORY ATTRIBUTE  >  MEMORY TYPE-119 (Custom Category) "+"\t"+custom_attribute_ram_type + "\n")
        f.write("CUSTOM CATEGORY ATTRIBUTE  >  SOCKET-346 (Custom Category) "+"\t"+cpu_socket + "\n")
        f.write("CUSTOM CATEGORY ATTRIBUTE  >  WATTAGES-355 (Custom Category) "+"\t"+custom_attribute_motherboard_wattage + "\n")


elif input_category == "4" or input_category.lower() == "graphics card":
    product_category="Graphics Card"
    print(f"You have selected {product_category}. Your Category is not available for this tool.")
    print("reach out to contact@sagarsardar.in for more information.")
elif input_category == "5" or input_category.lower() == "ram":
    product_category="RAM"
    print(f"You have selected {product_category}. Your Category is not available for this tool.")
    print("reach out to contact@sagarsardar.in for more information.") 
elif input_category == "6" or input_category.lower() == "storage":  
    product_category="Storage"
    print(f"You have selected {product_category}. Your Category is not available for this tool.")
    print("reach out to contact@sagarsardar.in for more information.")
elif input_category == "7" or input_category.lower() == "power supply":
    product_category="Power Supply"
    print(f"You have selected {product_category}. Your Category is not available for this tool.")
    print("reach out to contact@sagarsardar.in for more information.")  
elif input_category == "8" or input_category.lower() == "cabinet":
    product_category="Cabinet"
    print(f"You have selected {product_category}. Your Category is not available for this tool.")
    print("reach out to contact@sagarsardar.in for more information.")
elif input_category == "9" or input_category.lower() == "monitor":
    product_category="Monitor"
    print(f"You have selected {product_category}. Your Category is not available for this tool.")
    print("reach out to contact@sagarsardar.in for more information.")
elif input_category == "10" or input_category.lower() == "keyboard":
    product_category="Keyboard"
    print(f"You have selected {product_category}. Your Category is not available for this tool.")
    print("reach out to contact@sagarsardar.in for more information.")
elif input_category == "11" or input_category.lower() == "mouse":
    product_category="Mouse"
    print(f"You have selected {product_category}. Your Category is not available for this tool.")
    print("reach out to contact@sagarsardar.in for more information.")
elif input_category == "12" or input_category.lower() == "mouse pad":
    product_category="Mouse Pad"
    print(f"You have selected {product_category}. Your Category is not available for this tool.")
    print("reach out to contact@sagarsardar.in for more information.")
elif input_category == "13" or input_category.lower() == "headset":
    product_category="Headset"
    print(f"You have selected {product_category}. Your Category is not available for this tool.")
    print("reach out to contact@sagarsardar.in for more information.")
elif input_category == "14" or input_category.lower() == "speaker":
    product_category="Speaker"
    print(f"You have selected {product_category}. Your Category is not available for this tool.")
    print("reach out to contact@sagarsardar.in for more information.")
elif input_category == "15" or input_category.lower() == "thermal paste":
    product_category="Thermal Paste"
    print(f"You have selected {product_category}. Your Category is not available for this tool.")
    print("reach out to contact@sagarsardar.in for more information.")
elif input_category == "16" or input_category.lower() == "cables":
    product_category="Cables"
    print(f"You have selected {product_category}. Your Category is not available for this tool.")
    print("reach out to contact@sagarsardar.in for more information.")
elif input_category == "17" or input_category.lower() == "laptop":
    product_category="Laptop"
    print(f"You have selected {product_category}. Your Category is not available for this tool.")
    print("reach out to contact@sagarsardar.in for more information.")
elif input_category == "18" or input_category.lower() == "mini pc":
    product_category="Mini PC"
    print(f"You have selected {product_category}. Your Category is not available for this tool.")
    print("reach out to contact@sagarsardar.in for more information.")









