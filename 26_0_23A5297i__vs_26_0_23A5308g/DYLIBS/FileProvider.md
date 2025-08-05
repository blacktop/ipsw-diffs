## FileProvider

> `/System/Library/Frameworks/FileProvider.framework/FileProvider`

```diff

-3871.0.0.0.2
-  __TEXT.__text: 0x1323e4
+3882.0.36.0.0
+  __TEXT.__text: 0x1328d4
   __TEXT.__auth_stubs: 0x1d10
-  __TEXT.__objc_methlist: 0xe544
+  __TEXT.__objc_methlist: 0xe56c
   __TEXT.__const: 0x87e
   __TEXT.__gcc_except_tab: 0xa3b0
-  __TEXT.__cstring: 0x14562
+  __TEXT.__cstring: 0x145b2
   __TEXT.__oslogstring: 0xdc9b
   __TEXT.__dlopen_cstrs: 0x79f
   __TEXT.__ustring: 0x21e

   __TEXT.__swift5_types: 0x8
   __TEXT.__swift_as_entry: 0x4
   __TEXT.__swift_as_ret: 0x4
-  __TEXT.__unwind_info: 0x5920
+  __TEXT.__unwind_info: 0x5950
   __TEXT.__eh_frame: 0xa0
   __TEXT.__objc_classname: 0x2045
-  __TEXT.__objc_methname: 0x23d9f
+  __TEXT.__objc_methname: 0x23e68
   __TEXT.__objc_methtype: 0x68b6
-  __TEXT.__objc_stubs: 0x13dc0
-  __DATA_CONST.__got: 0xaa0
+  __TEXT.__objc_stubs: 0x13f40
+  __DATA_CONST.__got: 0xab8
   __DATA_CONST.__const: 0x6048
   __DATA_CONST.__objc_classlist: 0x690
   __DATA_CONST.__objc_catlist: 0x88
   __DATA_CONST.__objc_protolist: 0x2a0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x6d40
+  __DATA_CONST.__objc_selrefs: 0x6da0
   __DATA_CONST.__objc_protorefs: 0x158
   __DATA_CONST.__objc_superrefs: 0x550
   __DATA_CONST.__objc_arraydata: 0xab0
   __AUTH_CONST.__auth_got: 0xe98
-  __AUTH_CONST.__const: 0x1c08
-  __AUTH_CONST.__cfstring: 0x11120
+  __AUTH_CONST.__const: 0x1c28
+  __AUTH_CONST.__cfstring: 0x11140
   __AUTH_CONST.__objc_const: 0x247c8
   __AUTH_CONST.__objc_intobj: 0x108
   __AUTH_CONST.__objc_arrayobj: 0x198

   __AUTH.__data: 0x10
   __DATA.__objc_ivar: 0x1088
   __DATA.__data: 0x20c0
-  __DATA.__bss: 0xac0
+  __DATA.__bss: 0xa90
   __DATA.__common: 0x39
   __DATA_DIRTY.__objc_data: 0x3ca0
   __DATA_DIRTY.__data: 0x2c1
-  __DATA_DIRTY.__bss: 0x380
+  __DATA_DIRTY.__bss: 0x3c0
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/CoreServices

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
-  UUID: EA2299E1-7D09-3592-86D1-4AF8A556384B
-  Functions: 7241
-  Symbols:   23433
-  CStrings:  12267
+  UUID: 242AA4E6-5C16-3505-9FAE-F5D3E68ADFDE
+  Functions: 7251
+  Symbols:   23467
+  CStrings:  12281
 
Symbols:
+ -[FPTransformOperation copyItem:]
+ -[FPTrashOperation copyItem:]
+ -[FPUntrashOperation copyItem:]
+ -[NSString(FPAdditions) fp_getCrashDate]
+ -[NSString(FPAdditions) fp_getCrashDate].cold.1
+ _FPFileIsAlreadyPausedError_internal
+ _FPFileNotPausedError_internal
+ _FPTelemetryParsedError
+ _OBJC_CLASS_$_NSCalendar
+ _OBJC_CLASS_$_NSDateComponents
+ _OBJC_CLASS_$_NSRegularExpression
+ ___40-[NSString(FPAdditions) fp_getCrashDate]_block_invoke
+ ___block_descriptor_48_e8_32s40r_e19_24?0"FPItem"8Q16ls32l8r40l8
+ ___block_literal_global.133
+ ___block_literal_global.192
+ ___block_literal_global.201
+ ___block_literal_global.526
+ ___block_literal_global.94
+ _fp_getCrashDate.once
+ _fp_getCrashDate.regexp
+ _fpfs_fget_decmpf_info
+ _objc_msgSend$copyItem:
+ _objc_msgSend$currentCalendar
+ _objc_msgSend$dateFromComponents:
+ _objc_msgSend$firstMatchInString:options:range:
+ _objc_msgSend$rangeAtIndex:
+ _objc_msgSend$regularExpressionWithPattern:options:error:
+ _objc_msgSend$setDay:
+ _objc_msgSend$setHour:
+ _objc_msgSend$setMinute:
+ _objc_msgSend$setMonth:
+ _objc_msgSend$setSecond:
+ _objc_msgSend$setYear:
- ___block_descriptor_48_e8_32s40r_e19_24?0"FPItem"8Q16lr40l8s32l8
- ___block_literal_global.125
- ___block_literal_global.184
- ___block_literal_global.193
- ___block_literal_global.525
CStrings:
+ "([0-9][0-9][0-9][0-9])-([0-1][0-9])-([0-3][0-9])-([0-2][0-9])([0-5][0-9])([0-5][0-9])"
+ "3882.0.36"
+ "copyItem:"
+ "currentCalendar"
+ "dateFromComponents:"
+ "firstMatchInString:options:range:"
+ "fp_getCrashDate"
+ "rangeAtIndex:"
+ "regularExpressionWithPattern:options:error:"
+ "setDay:"
+ "setHour:"
+ "setMinute:"
+ "setMonth:"
+ "setYear:"
- "3871.0.0.0.2"

```
