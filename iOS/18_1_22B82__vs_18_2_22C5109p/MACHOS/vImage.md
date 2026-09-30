## vImage

> `/System/ExclaveKit/System/Library/Frameworks/Accelerate.framework/Frameworks/vImage.framework/vImage`

```diff

-601.40.5.0.0
-  __TEXT.__text: 0x19b28
-  __TEXT.__auth_stubs: 0xc0
-  __TEXT.__const: 0x1b4
-  __TEXT.__unwind_info: 0xe8
+602.60.7.0.0
+  __TEXT.__text: 0x1a998
+  __TEXT.__auth_stubs: 0xf0
+  __TEXT.__const: 0x1c4
+  __TEXT.__unwind_info: 0x100
   __TEXT.__eh_frame: 0x60
-  __DATA.__auth_got: 0x60
+  __DATA.__auth_got: 0x78
   __DATA.__got: 0x8
-  __DATA.__auth_ptr: 0x8
+  __DATA.__auth_ptr: 0x10
+  __DATA.__bss: 0x20
+  - /System/ExclaveKit/System/Library/Frameworks/MobileGestalt.framework/MobileGestalt
   - /System/ExclaveKit/usr/lib/libSystem.dylib
   Functions: 37
-  Symbols:   49
+  Symbols:   53
   CStrings:  0
 
Symbols:
+ _CoefGenerationVertical_64x16
+ _CoefGeneration_64x16
+ _Init_gAMXVersion
+ _MobileGestalt_get_AMXVersion
+ _MobileGestalt_get_current_device
+ __MergedGlobals
+ _dispatch_once_f
+ _vHorizontal_Scale_Planar_UInt8_Accelerate_64x16
+ _vImageGetResamplingFilterSize
+ _vVertical_Scale_Planar_UInt8_Accelerate_64x16
- _sVertical_Scale_Planar_UInt8
- _sVertical_Shear_Planar_UInt8
- _vHorizontal_Shear_Planar_UInt8
- _vRotate_90_ARGB_8888
- _vRotate_90_Planar_UInt8
- _vVertical_Shear_Planar_UInt8

```
