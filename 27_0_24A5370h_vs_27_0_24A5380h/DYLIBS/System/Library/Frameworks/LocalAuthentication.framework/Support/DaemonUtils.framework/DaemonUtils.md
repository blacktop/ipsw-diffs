## DaemonUtils

> `/System/Library/Frameworks/LocalAuthentication.framework/Support/DaemonUtils.framework/DaemonUtils`

```diff

-  __TEXT.__text: 0x8dbc
-  __TEXT.__objc_methlist: 0x1258
-  __TEXT.__const: 0x160
-  __TEXT.__cstring: 0x595
-  __TEXT.__oslogstring: 0xa0b
-  __TEXT.__gcc_except_tab: 0xc4
-  __TEXT.__unwind_info: 0x3b0
+  __TEXT.__text: 0x8aa8
+  __TEXT.__objc_methlist: 0x1230
+  __TEXT.__const: 0x170
+  __TEXT.__cstring: 0x553
+  __TEXT.__oslogstring: 0x997
+  __TEXT.__gcc_except_tab: 0xd0
+  __TEXT.__unwind_info: 0x3a0
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0

   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x50
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0xaf0
+  __DATA_CONST.__objc_selrefs: 0xad8
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x58
   __DATA_CONST.__objc_arraydata: 0x30
-  __DATA_CONST.__got: 0x210
-  __AUTH_CONST.__const: 0x240
-  __AUTH_CONST.__cfstring: 0x620
+  __DATA_CONST.__got: 0x228
+  __AUTH_CONST.__const: 0x1e0
+  __AUTH_CONST.__cfstring: 0x5e0
   __AUTH_CONST.__objc_const: 0x2b00
   __AUTH_CONST.__objc_intobj: 0xd8
   __AUTH_CONST.__objc_arrayobj: 0x30
-  __AUTH_CONST.__auth_got: 0x2b8
+  __AUTH_CONST.__auth_got: 0x2c0
   __DATA.__objc_ivar: 0x160
   __DATA.__data: 0x3c0
-  __DATA.__bss: 0x50
+  __DATA.__bss: 0x28
   __DATA_DIRTY.__objc_data: 0x410
-  __DATA_DIRTY.__bss: 0xd0
+  __DATA_DIRTY.__bss: 0xc8
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices
   - /System/Library/Frameworks/Foundation.framework/Foundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 347
-  Symbols:   1439
-  CStrings:  168
+  Functions: 335
+  Symbols:   1408
+  CStrings:  161
 
Sections:
~ __DATA_CONST.__const : content changed
~ __DATA_CONST.__objc_classlist : content changed
~ __DATA_CONST.__objc_catlist : content changed
~ __DATA_CONST.__objc_protolist : content changed
~ __DATA_CONST.__objc_protorefs : content changed
~ __DATA_CONST.__objc_superrefs : content changed
~ __DATA_CONST.__objc_arraydata : content changed
~ __AUTH_CONST.__objc_const : content changed
~ __AUTH_CONST.__objc_intobj : content changed
~ __AUTH_CONST.__objc_arrayobj : content changed
~ __DATA.__data : content changed
~ __DATA_DIRTY.__objc_data : content changed
Symbols:
+ -[LAAnalyticsDTO _skipRetryInterval]
+ GCC_except_table11
+ GCC_except_table17
+ _LACErrorCodeInternal
+ _LACLogPushButton
+ _OBJC_CLASS_$_LACError
+ _OBJC_CLASS_$_LACMobileGestalt
+ _objc_msgSend$_skipRetryInterval
+ _objc_msgSend$errorWithCode:debugDescription:
- +[DaemonUtils deviceHasSecureDoublePressHW]
- +[DaemonUtils deviceHasSpecialTouchID]
- +[DaemonUtils deviceHasTouchIDAndSecureDoublePress]
- +[DaemonUtils deviceIsPoseidon]
- +[DaemonUtils deviceSupportsSecureDoubleClick]
- GCC_except_table12
- ___43+[DaemonUtils deviceHasSecureDoublePressHW]_block_invoke
- ___46+[DaemonUtils deviceSupportsSecureDoubleClick]_block_invoke
- _deviceHasSecureDoublePressHW.hasSecureDoublePressHW
- _deviceHasSecureDoublePressHW.onceToken
- _deviceSupportsSecureDoubleClick.onceToken
- _deviceSupportsSecureDoubleClick.supportsSecureDoubleClick
- _objc_msgSend$deviceHasSecureDoublePressHW
- _objc_msgSend$deviceHasTouchID
- _objc_msgSend$deviceSupportsSecureDoubleClick
- _objc_msgSend$internalErrorWithMessage:
CStrings:
- "Can't query SecureDoubleClick."
- "DeviceSupportsSecureDoubleClick"
- "HardwareSupportsSecureDoubleClick"
- "deviceHasSecureDoublePressHW returned %d"
- "deviceSupportsSecureDoubleClick returned %d"

```
