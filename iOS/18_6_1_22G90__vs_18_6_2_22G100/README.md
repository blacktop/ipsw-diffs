# 18.6.1 (22G90) .vs 18.6.2 (22G100)

## Security Content

- <https://support.apple.com/en-us/124925>

## IPSWs

- `iPhone17,1_18.6.1_22G90_Restore.ipsw`
- `iPhone17,1_18.6.2_22G100_Restore.ipsw`

## Kernel

### Version

| iOS | Version | Build | Date |
| :-- | :------ | :---- | :--- |
| 18.6.1 *(22G90)* | 24.6.0 | 11417.140.69~16 | Tue, 15Jul2025 21:54:57 PDT |
| 18.6.2 *(22G100)* | 24.6.0 | 11417.140.69~16 | Tue, 15Jul2025 21:54:57 PDT |

### iBoot

| iOS | Version |
| :-- | :------ |
| 18.6.1 *(22G90)* | iBoot-11881.140.96 |
| 18.6.2 *(22G100)* | iBoot-11881.140.96 |

## DSC

### WebKit

| iOS | Version |
| :-- | :------ |
| 18.6.1 *(22G90)* | 621.3.11.10.3 |
| 18.6.2 *(22G100)* | 621.3.11.10.3 |

### Dylibs

#### ⬆️ Updated (1)

<details>
  <summary><i>View Updated</i></summary>

#### RawCamera

>  `/System/Library/CoreServices/RawCamera.bundle/RawCamera`

```diff

-1738.140.3.0.0
-  __TEXT.__text: 0x1e2d70
-  __TEXT.__auth_stubs: 0x1850
+1738.140.3.0.11
+  __TEXT.__text: 0x1e3470
+  __TEXT.__auth_stubs: 0x1870
   __TEXT.__objc_methlist: 0x16e4
   __TEXT.__const: 0x15326
-  __TEXT.__gcc_except_tab: 0x2d440
+  __TEXT.__gcc_except_tab: 0x2d588
   __TEXT.__oslogstring: 0xec0
   __TEXT.__cstring: 0xee23
   __TEXT.__dof_RawCamera: 0x8f7
-  __TEXT.__unwind_info: 0xb1d0
+  __TEXT.__unwind_info: 0xb1e8
   __TEXT.__eh_frame: 0x278
   __TEXT.__objc_classname: 0x4b9
   __TEXT.__objc_methname: 0x3918
   __TEXT.__objc_methtype: 0xdd3
   __TEXT.__objc_stubs: 0x2da0
-  __DATA_CONST.__got: 0x9b0
+  __DATA_CONST.__got: 0x9c8
   __DATA_CONST.__const: 0x2a18
   __DATA_CONST.__objc_classlist: 0x1e0
   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0xcf8
   __DATA_CONST.__objc_superrefs: 0xf0
-  __DATA_CONST.__objc_arraydata: 0x3948
-  __AUTH_CONST.__auth_got: 0xc40
+  __DATA_CONST.__objc_arraydata: 0x3950
+  __AUTH_CONST.__auth_got: 0xc50
   __AUTH_CONST.__const: 0x35978
   __AUTH_CONST.__cfstring: 0x18080
   __AUTH_CONST.__objc_const: 0x48b0
-  __AUTH_CONST.__objc_arrayobj: 0x570
-  __AUTH_CONST.__objc_intobj: 0x39f0
+  __AUTH_CONST.__objc_arrayobj: 0x588
+  __AUTH_CONST.__objc_intobj: 0x3a20
   __AUTH_CONST.__objc_doubleobj: 0x480
   __AUTH_CONST.__objc_dictobj: 0x4d58
   __AUTH_CONST.__objc_floatobj: 0xc0

   - /System/Library/Frameworks/UniformTypeIdentifiers.framework/UniformTypeIdentifiers
   - /System/Library/PrivateFrameworks/AppleJPEG.framework/AppleJPEG
   - /System/Library/PrivateFrameworks/AppleJPEGXL.framework/AppleJPEGXL
+  - /System/Library/PrivateFrameworks/CMPhoto.framework/CMPhoto
   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/CoreAnalytics
   - /System/Library/PrivateFrameworks/MobileAsset.framework/MobileAsset
   - /usr/lib/libSystem.B.dylib

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libxml2.2.dylib
   - /usr/lib/libz.1.dylib
-  UUID: 1BE38EB6-51C0-3069-A50F-CA3B000E0847
-  Functions: 6433
-  Symbols:   781
+  UUID: AF5B7B35-3549-329B-B706-F877FA8DF849
+  Functions: 6435
+  Symbols:   786
   CStrings:  7487
 
Symbols:
+ _CMPhotoDecompressionContainerCreateImageForIndex
+ _CMPhotoDecompressionContainerGetImageCount
+ _CMPhotoDecompressionSessionCreate
+ _CMPhotoDecompressionSessionCreateContainer
+ _CVPixelBufferGetDataSize
+ _kCMPhotoContainerFormatString_JFIF
+ _kCMPhotoDecompressionContainerOption_AllowedFormatsAndCodecs
+ _kCMPhotoDecompressionOption_OutputPixelFormat
- _CGImageGetBytesPerRow
- _CGImageGetHeight
- _CGImageGetWidth

```


</details>

## EOF
