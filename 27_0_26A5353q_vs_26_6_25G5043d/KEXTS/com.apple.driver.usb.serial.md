## com.apple.driver.usb.serial

> `com.apple.driver.usb.serial`

```diff

-153.0.0.0.0
+145.160.2.0.0
   __TEXT.__const: 0x60 sha256:d13240e5e5454416bcbf74c570602012bcd579e7470fb38ac4b0f4c5b1c119b2
-  __TEXT.__cstring: 0x235 sha256:4a1b4f808234b234266a3c81e7a4373121e231915043506509fbc34c128f77ed
-  __TEXT_EXEC.__text: 0x5788 sha256:cd6cde22d2f1ae1842623308b824b8310ce60bda0543af0c93bfe6429efdaab4
+  __TEXT.__cstring: 0x1ff sha256:e5082c4a1b3ac0d4604a50e2771e07884e9d278d42ace03eaab5a295ca666d68
+  __TEXT_EXEC.__text: 0x557c sha256:6a6f499d93da17d083958459f547b9f276febea3447bbb20c55d0e5cfebf1bd4
   __TEXT_EXEC.__auth_stubs: 0x0
-  __DATA.__data: 0xc8 sha256:fc9d52e0467f834994fd6d315262f02692ed1a96bb05ba97634fb4d3e0120ccc
+  __DATA.__data: 0xc8 sha256:fdad52e253d48372636ea5eba8b9e27e56523ac8ffc6efef90ec3d68bb618b6a
   __DATA.__common: 0x60 sha256:2ea9ab9198d1638007400cd2c3bef1cc745b864b76011a0e1bc52180ac6452d4
-  __DATA_CONST.__mod_init_func: 0x8 sha256:10a2e3f28240ae9b1e46bdc75bd43044b847080b8ca17f9c2c5fe2f97e46b609
-  __DATA_CONST.__mod_term_func: 0x8 sha256:938a2fe67cc91edebb896afc41cf8c789eb2df4a56dfd948ad9daf5c7c954977
-  __DATA_CONST.__const: 0x1608 sha256:08f9f1e37be9aa0a6a87ee4cf6c6a210190420c253d9f47068047500dfd1f5e9
-  __DATA_CONST.__kalloc_type: 0x80 sha256:1d5a918ed3af5250d05afe014975f06391d58e94faadea0d8c94ce1fe7ccaf64
-  __DATA_CONST.__kalloc_var: 0x140 sha256:71d1fb63a8fdc71dc9074541c716ee5bc575bad0729eb720ffcb33e9119bdb36
-  __DATA_CONST.__auth_got: 0x130 sha256:bf1375b11dba5583c493360ee8084f58eb0d0f2b4a10b7f54d77de20cefa14c9
-  __DATA_CONST.__got: 0x70 sha256:c7d33467f3d4ca31ce84f49bc680a1565b608b75fb738d11479a5bea4de4106d
-  UUID: 6BD2D092-87AA-3EC5-9710-384E130DC2FD
+  __DATA_CONST.__auth_got: 0x118 sha256:6333e80d632f163bf3dccbc726cb5e8f48c7bb9137db080d03d42464013fbb14
+  __DATA_CONST.__got: 0x68 sha256:03f27aaa21fbf8498515cafd3ffc507ef6392a6e39f6b16e317cb8b0e9c4efe2
+  __DATA_CONST.__mod_init_func: 0x8 sha256:44ea5871200dfb47be340e63b433fedca3093c9bba15b14922af897b11b7df97
+  __DATA_CONST.__mod_term_func: 0x8 sha256:86fdcf19c63475bc41107ac869080e27f8c2c82150b857279544d914fe308f6c
+  __DATA_CONST.__const: 0x1608 sha256:08d80057d4989bbb2756aa77958309e043dbe3398edd09d4f0a6b9e383f3a756
+  __DATA_CONST.__kalloc_type: 0x80 sha256:e8c1aa900101a7ccfba2d3670bd124e5f482f69da0fb61cfff248dc198e14889
+  __DATA_CONST.__kalloc_var: 0x140 sha256:c98ba4e2e7a8bc0fef02834ad6886048aca710768674b6e681735037065fb02d
+  UUID: EE106984-9849-3741-889B-A72509132250
   Functions: 117
-  Symbols:   532
-  CStrings:  26
+  Symbols:   528
+  CStrings:  25
 
Symbols:
+ __ZZN14AppleUSBSerial13freeResourcesEvE20kalloc_type_view_564
+ __ZZN14AppleUSBSerial13freeResourcesEvE20kalloc_type_view_573
+ __ZZN14AppleUSBSerial14allocResourcesEhhP24IOBufferMemoryDescriptorS1_jjE20kalloc_type_view_525
+ __ZZN14AppleUSBSerial14allocResourcesEhhP24IOBufferMemoryDescriptorS1_jjE20kalloc_type_view_528
- __ZZN14AppleUSBSerial13freeResourcesEvE20kalloc_type_view_586
- __ZZN14AppleUSBSerial13freeResourcesEvE20kalloc_type_view_595
- __ZZN14AppleUSBSerial14allocResourcesEhhP24IOBufferMemoryDescriptorS1_jjE20kalloc_type_view_547
- __ZZN14AppleUSBSerial14allocResourcesEhhP24IOBufferMemoryDescriptorS1_jjE20kalloc_type_view_550
- _kdebug_enable
- _kernel_debug
- _kernel_debug_filtered
- _strtoul
CStrings:
+ "AppleUSBSerial::armRead() - no space left\n"
- "AppleUSBSerial::armRead() - %u bytes were dropped\n"
- "AppleUSBSerial::armRead() - no space left %d\n"

```
