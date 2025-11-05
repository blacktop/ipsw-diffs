## ZoomServices

> `/System/iOSSupport/System/Library/PrivateFrameworks/ZoomServices.framework/Versions/A/ZoomServices`

```diff

-3148.7.15.0.0
-  __TEXT.__text: 0x5210
+3148.15.11.1.0
+  __TEXT.__text: 0x51f4
   __TEXT.__auth_stubs: 0x4f0
-  __TEXT.__objc_methlist: 0x59c
+  __TEXT.__objc_methlist: 0x704
   __TEXT.__const: 0x40
   __TEXT.__gcc_except_tab: 0x14
   __TEXT.__cstring: 0x7db
   __TEXT.__oslogstring: 0x4c
-  __TEXT.__unwind_info: 0x1e0
+  __TEXT.__unwind_info: 0x1d8
   __TEXT.__objc_classname: 0x91
   __TEXT.__objc_methname: 0x174e
   __TEXT.__objc_methtype: 0x4ae

   __DATA_CONST.__objc_classlist: 0x20
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x590
+  __DATA_CONST.__objc_selrefs: 0x650
   __DATA_CONST.__objc_superrefs: 0x8
   __DATA_CONST.__objc_arraydata: 0x50
   __AUTH_CONST.__auth_got: 0x288
   __AUTH_CONST.__const: 0x80
   __AUTH_CONST.__cfstring: 0x6e0
-  __AUTH_CONST.__objc_const: 0x8e0
+  __AUTH_CONST.__objc_const: 0x640
   __AUTH_CONST.__objc_dictobj: 0x78
   __AUTH_CONST.__objc_intobj: 0xd8
   __AUTH_CONST.__objc_arrayobj: 0x18

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 388561E6-2ECF-3CA4-8167-011BC94B0EE3
+  UUID: 9099932D-D95D-3F15-91DF-4CF043B57BBE
   Functions: 138
-  Symbols:   470
+  Symbols:   472
   CStrings:  424
 
Symbols:
+ +[ZoomServices sharedInstance].cold.1
+ ZOTMainScreenSize.cold.1
Functions:
~ +[ZoomServices sharedInstance] : 84 -> 68
~ __registerObservers : 120 -> 112
~ ___48-[ZoomServices registerInterestInZoomAttributes]_block_invoke : 208 -> 204
~ _ZOTMainScreenSize : 76 -> 64
~ -[ZoomServicesKeyboardManager keyboardCommandForEvent:] : 1132 -> 1136
~ sub_2716170d0 -> -[ZoomServicesKeyboardManager inUnitTestMode] : 16 -> 8
~ sub_2716170e0 -> -[ZoomServicesKeyboardManager setInUnitTestMode:] : 16 -> 8
~ -[ZoomServicesKeyboardManager inUnitTestMode] -> +[ZoomServices sharedInstance].cold.1 : 8 -> 20
~ -[ZoomServicesKeyboardManager setInUnitTestMode:] -> ZOTMainScreenSize.cold.1 : 8 -> 20
CStrings:
+ "/AppleInternal/Library/BuildRoots/01adf19d-fba1-11ef-a947-f2a857e00a32/Library/Caches/com.apple.xbs/Sources/AccessibilityFrameworks/AccessibilityUmbrellaFramework/Frameworks/ZoomServices/Source/ZoomServices.m"
- "/AppleInternal/Library/BuildRoots/91509d18-d3bf-11ef-a177-d285688f7a47/Library/Caches/com.apple.xbs/Sources/AccessibilityFrameworks/AccessibilityUmbrellaFramework/Frameworks/ZoomServices/Source/ZoomServices.m"

```
