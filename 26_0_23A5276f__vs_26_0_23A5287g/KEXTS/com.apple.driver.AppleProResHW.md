## com.apple.driver.AppleProResHW

> `com.apple.driver.AppleProResHW`

```diff

-500.55.0.0.0
-  __TEXT.__const: 0x2090
-  __TEXT.__os_log: 0x8711
-  __TEXT.__cstring: 0xf6c
-  __TEXT_EXEC.__text: 0x37c50
+500.71.0.0.0
+  __TEXT.__const: 0x2198
+  __TEXT.__os_log: 0x933b
+  __TEXT.__cstring: 0xf8b
+  __TEXT_EXEC.__text: 0x39b2c
   __TEXT_EXEC.__auth_stubs: 0x0
-  __DATA.__data: 0x3a8
+  __DATA.__data: 0x3b8
   __DATA.__common: 0x70
   __DATA.__bss: 0x62c0
   __DATA_CONST.__auth_got: 0x280

   __DATA_CONST.__const: 0x9e68
   __DATA_CONST.__kalloc_type: 0x480
   __DATA_CONST.__kalloc_var: 0x140
-  UUID: 7B1E71E6-1C45-3F48-ACDA-33F108498E17
-  Functions: 1836
+  UUID: 709C667C-2F6D-3A71-ACE6-B81E72E1863B
+  Functions: 1839
   Symbols:   0
-  CStrings:  505
+  CStrings:  512
 
CStrings:
+ "121111121222121211221111211111121111112111111211222211112222211112111111211111121111112111111111111111111111111111111121121121121111111111111111111111111111111111111111111111111111111111111111111112222222222222222221111111222211111111111121222211112"
+ "AppleProResHW (0x%x): %s(): CFA=%d Data/Stride R=%p,%u\n"
+ "AppleProResHW (0x%x): %s(): Data/Stride R=%p,%u Gr=%p,%u Gb=%p,%u B=%p,%u Plane Count=%d CFA=%d\n"
+ "AppleProResHW (0x%x): %s(): DecodeRaw cmd: fid=%d SwBR=%d 2raw=%d Int=%d dec=%d ga=%d cmpGaEn=%d ds=%d bd=%d cmd-word %08x cmdX-word %08x pk=%d iv=%d cpd=%d FO=%d Fld=%d\n"
+ "AppleProResHW (0x%x): %s(): DecodeRaw: CFA=%d Data/Stride R=%p, %u, Gr=%p,%u Gb=%p,%u B=%p,%u\n"
+ "AppleProResHW (0x%x): %s(): DecodeYCbCr cmd: fid=%d bff=%d 2raw=%d Int=%d dec=%d a=%d cmp=%d ds=%d cfmt=%d bd=%d cmd-word=%08x cmdX-word=%08x LCA=%d LCC=%d LCY=%d afill=0x%x\n"
+ "AppleProResHW (0x%x): %s(): EncodeYCbCr cmd: fid=%d fstpss=%d Int=%d enc=%d a=%d cmp=%d nPass=%d cfmt=%d bd=%d. Program Output DartVA %p Address=%08x.%08x MaxSize=%u Input OffsetH,V=%u,%u SizeH,V=%u,%u Width=%u Height=%u cmd-word %08x\ncmdX-word %08x LCA=%d LCC=%d LCY=%d BrWrDis=%d\n"
+ "AppleProResHW (0x%x): %s(): FrameHeader size=%u ver=%u id=%u hsize=%u vsize=%u crop={%u,%u,%u,%u} cfa=%u svr=%u wbr=%u wbb=%u cm={%u,%u,%u,%u,%u,%u,%u,%u,%u} gf=%u wbcct=%u hme=%u ltf=%u dss=%u lqm=%u tf={%u,%u,%u,%u,%u,%u,%u,%u} QuantizationScaling scale=%u CRC Enable/Reset=%x QuantizationMatrix idx=%u\n"
+ "AppleProResHW (0x%x): %s(): Single plane bp16 case, Data/Stride R=%p,%u, Plane Count=%d CFA=%d\n"
+ "AppleProResHW (0x%x): %s(): frameId=%d intEn=%d encMode=%d cmpGaEn=%d passes=%d fastPass=%d bitDepth=%d. Output DartVA=%p Address=%08x.%08x Size=%u Input OffsetH,V=%u,%u SizeH,V=%u,%u Width,Height=%u,%u cmd-word %08x cmdX-word %08x Pkd=%d Ivd=%d Cmpd=%d FO=%d Fld=%d\n"
+ "AppleProResHW (0x%x): %s(): override: Compressed=0x%x Packed=0x%x, Interleaved=0x%x Folded=0x%x"
+ "ERROR AppleProResHW (0x%x): %d: %s(): No cores powered on.\n"
+ "ERROR AppleProResHW (0x%x): %d: %s(): Program DecodeRAW Descriptor failed\n"
+ "ERROR AppleProResHW (0x%x): %d: %s(): Program EncodeRAW Descriptor failed\n"
+ "ERROR AppleProResHW (0x%x): %d: %s(): Unsupported CFApattern %d\n"
+ "ProgramDecodeRawDescriptor"
+ "p0"
- "12111112122212121122111121111112111111211111121122221111222221111211111121111112111111211111111111111111111111111111112112112112111111111111111111111111111111111111111111111111111111111111111111111222222222222222221111111222211111111111121222211112"
- "AppleProResHW (0x%x): %s(): Data/Stride R=%p,%u\n"
- "AppleProResHW (0x%x): %s(): Data/Stride R=%p,%u Gr=%p,%u Gb=%p,%u B=%p,%u\n"
- "AppleProResHW (0x%x): %s(): DecodeRaw cmd: fid=%d SwBR=%d 2raw=%d Int=%d dec=%d Graw=%d ds=%d bd=%d cmd-word %08x pk=%d iv=%d cpd=%d FO=%d\n"
- "AppleProResHW (0x%x): %s(): DecodeRaw: Data/Stride R=%p, %u, Gr=%p,%u Gb=%p,%u B=%p,%u\n"
- "AppleProResHW (0x%x): %s(): DecodeYCbCr cmd: fid=%d bff=%d 2raw=%d Int=%d dec=%d a=%d Graw=%d ds=%d cfmt=%d bd=%d cmd-word=%08x LCA=%d LCC=%d LCY=%d afill=0x%x\n"
- "AppleProResHW (0x%x): %s(): EncodeYCbCr cmd: fid=%d fstpss=%d Int=%d enc=%d a=%d Graw=%d nPass=%d cfmt=%d bd=%d. Program Output DartVA %p Address=%08x.%08x MaxSize=%u Input OffsetH,V=%u,%u SizeH,V=%u,%u Width=%u Height=%u cmd-word %08x\nLCA=%d LCC=%d LCY=%d BrWrDis=%d\n"
- "AppleProResHW (0x%x): %s(): FrameHeader size=%u ver=%u id=%u hsize=%u vsize=%u crop={%u,%u,%u,%u} bp=%u svr=%u wbr=%u wbb=%u cm={%u,%u,%u,%u,%u,%u,%u,%u,%u} gf=%u wbcct=%u hme=%u ltf=%u dss=%u lqm=%u tf={%u,%u,%u,%u,%u,%u,%u,%u} QuantizationScaling scale=%u CRC Enable/Reset=%x QuantizationMatrix idx=%u\n"
- "AppleProResHW (0x%x): %s(): Single plane bp16 case, Data/Stride R=%p,%u, BP %d \n"
- "AppleProResHW (0x%x): %s(): frameId=%d intEn=%d encMode=%d gammaEn=%d passes=%d fastPass=%d bitDepth=%d. Output DartVA=%p Address=%08x.%08x Size=%u Input OffsetH,V=%u,%u SizeH,V=%u,%u Width,Height=%u,%u cmd-word %08x Pkd=%d Ivd=%d Cmpd=%d FO=%d\n"

```
