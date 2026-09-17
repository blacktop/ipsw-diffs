## H16ISP.mediacapture

> `/System/Library/MediaCapture/H16ISP.mediacapture`

```diff

-6.20.0.0.0
-  __TEXT.__text: 0x193ae0
-  __TEXT.__const: 0x2ddc8
-  __TEXT.__oslogstring: 0x18d14
-  __TEXT.__cstring: 0x1568f
+6.103.0.0.0
+  __TEXT.__text: 0x193bf4
+  __TEXT.__const: 0x2ddb2
+  __TEXT.__oslogstring: 0x18d65
+  __TEXT.__cstring: 0x1565d
   __TEXT.__gcc_except_tab: 0x46c4
-  __TEXT.__unwind_info: 0x53f0
+  __TEXT.__unwind_info: 0x53f8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_methname: 0x0
-  __DATA_CONST.__const: 0xb9d0
+  __DATA_CONST.__const: 0xb9e0
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x18
-  __DATA_CONST.__objc_selrefs: 0x270
+  __DATA_CONST.__objc_selrefs: 0x288
   __DATA_CONST.__objc_arraydata: 0x8
   __DATA_CONST.__got: 0x0
-  __AUTH_CONST.__const: 0x25e8
-  __AUTH_CONST.__cfstring: 0x7360
+  __AUTH_CONST.__const: 0x25c8
+  __AUTH_CONST.__cfstring: 0x73c0
   __AUTH_CONST.__weak_auth_got: 0xa0
   __AUTH_CONST.__objc_arrayobj: 0x18
   __AUTH_CONST.__objc_intobj: 0x30
   __AUTH_CONST.__auth_got: 0x1380
   __DATA.__data: 0x382408
   __DATA.__common: 0x14
-  __DATA_DIRTY.__data: 0x1b0
-  __DATA_DIRTY.__bss: 0x920
+  __DATA_DIRTY.__data: 0x1b8
+  __DATA_DIRTY.__bss: 0x930
   - /System/Library/Frameworks/Accelerate.framework/Versions/A/Accelerate
   - /System/Library/Frameworks/AudioToolbox.framework/Versions/A/AudioToolbox
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libz.1.dylib
   Functions: 4979
-  Symbols:   7597
-  CStrings:  5442
+  Symbols:   7600
+  CStrings:  5444
 
Symbols:
+ _ZN6H16ISP12SystemStatus26CopyBuiltInCameraDeviceUIDEv
+ __DefaultRuneLocale
+ __ZN6H16ISP12H16ISPDevice35InvokeDeviceMessageNotificationProcEjPv
+ __ZN6H16ISP12SystemStatus26CopyBuiltInCameraDeviceUIDEv
+ __oidAppleExtendedKeyUsageSWUpdateSigning
+ _objc_msgSend$characterAtIndex:
+ _objc_msgSend$componentsSeparatedByString:
+ _objc_msgSend$count
+ _oidAppleExtendedKeyUsageSWUpdateSigning
+ _os_unfair_lock_lock
+ _os_unfair_lock_unlock
- _ZN6H16ISP12SystemStatus17CopyCMIODeviceUIDEv
- __ZN6H16ISP12SystemStatus17CopyCMIODeviceUIDEv
- __ZZN6H16ISP12SystemStatus17CopyCMIODeviceUIDEvE9fnGetData
- __ZZN6H16ISP12SystemStatus17CopyCMIODeviceUIDEvE9fnGetSize
- __ZZN6H16ISP12SystemStatus17CopyCMIODeviceUIDEvE9onceToken
- ____ZN6H16ISP12SystemStatus17CopyCMIODeviceUIDEv_block_invoke
- _dlopen
- _dlsym
CStrings:
+ "%08X-%04X-%04X-%04X-%012X"
+ "%s - CopyBuiltInCameraDeviceUID returned NULL on macOS — falling back to \"0\"; privacy indicator may not engage.\n"
+ "%s - CopyBuiltInCameraDeviceUID: unexpected kMGQProductType=%{public}@\n"
+ ","
+ "CopyBuiltInCameraDeviceUID"
+ "ProductType"
- "%s - CopyCMIODeviceUID returned NULL on macOS — falling back to \"0\". Privacy indicator may not engage.\n"
- "/System/Library/Frameworks/CoreMediaIO.framework/CoreMediaIO"
- "CMIOObjectGetPropertyData"
- "CMIOObjectGetPropertyDataSize"
```
