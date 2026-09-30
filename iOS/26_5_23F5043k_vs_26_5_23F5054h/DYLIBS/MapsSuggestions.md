## MapsSuggestions

> `/System/Library/PrivateFrameworks/MapsSuggestions.framework/MapsSuggestions`

```diff

-2921.35.2.9.18
-  __TEXT.__text: 0x184918
+2921.35.2.9.24
+  __TEXT.__text: 0x184900
   __TEXT.__auth_stubs: 0x1bb0
   __TEXT.__objc_methlist: 0x9dd0
   __TEXT.__const: 0x1468
-  __TEXT.__gcc_except_tab: 0x152c0
-  __TEXT.__cstring: 0x2bd30
-  __TEXT.__oslogstring: 0x1635f
+  __TEXT.__gcc_except_tab: 0x152bc
+  __TEXT.__cstring: 0x2bd40
+  __TEXT.__oslogstring: 0x1636f
   __TEXT.__ustring: 0x39c
   __TEXT.__dlopen_cstrs: 0xb0
   __TEXT.__swift5_typeref: 0xdee

   __TEXT.__swift_as_ret: 0x5c
   __TEXT.__swift5_proto: 0x14
   __TEXT.__swift5_protos: 0x4
-  __TEXT.__unwind_info: 0x63e0
+  __TEXT.__unwind_info: 0x63e8
   __TEXT.__eh_frame: 0xf70
   __TEXT.__objc_classname: 0x2f6b
-  __TEXT.__objc_methname: 0x151c1
+  __TEXT.__objc_methname: 0x15161
   __TEXT.__objc_methtype: 0x6dfb
-  __TEXT.__objc_stubs: 0xbe80
+  __TEXT.__objc_stubs: 0xbe40
   __DATA_CONST.__got: 0x1048
-  __DATA_CONST.__const: 0xf1d8
+  __DATA_CONST.__const: 0xf200
   __DATA_CONST.__objc_classlist: 0x7a0
   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_protolist: 0x370
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x4730
+  __DATA_CONST.__objc_selrefs: 0x4720
   __DATA_CONST.__objc_protorefs: 0x148
   __DATA_CONST.__objc_superrefs: 0x438
   __DATA_CONST.__objc_arraydata: 0x88
   __AUTH_CONST.__auth_got: 0xdf0
   __AUTH_CONST.__const: 0x84e8
-  __AUTH_CONST.__cfstring: 0xdfa0
-  __AUTH_CONST.__objc_const: 0x17720
+  __AUTH_CONST.__cfstring: 0xdf80
+  __AUTH_CONST.__objc_const: 0x17740
   __AUTH_CONST.__objc_intobj: 0x798
   __AUTH_CONST.__objc_dictobj: 0x78
   __AUTH_CONST.__objc_arrayobj: 0x48

   __AUTH_CONST.__objc_floatobj: 0xd0
   __AUTH.__objc_data: 0x10b8
   __AUTH.__data: 0x288
-  __DATA.__objc_ivar: 0x974
+  __DATA.__objc_ivar: 0x978
   __DATA.__data: 0x28d8
   __DATA.__bss: 0x710
   __DATA.__common: 0xa8

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  UUID: B45518B6-1066-320F-BCAD-D30715660D8C
+  UUID: 43A86BA9-D6BA-3BD8-9956-F49BEB4CE2C0
   Functions: 6253
-  Symbols:   19270
-  CStrings:  11589
+  Symbols:   19271
+  CStrings:  11587
 
Symbols:
+ _OBJC_IVAR_$_MapsSuggestionsXPCActivityTimer._taskCompleted
+ ___67-[MapsSuggestionsXPCActivityTimer scheduleWithTimeInterval:leeway:]_block_invoke.135
+ ___block_descriptor_40_ea8_32w_e22_v16?0"BGSystemTask"8lw32l8
+ ___block_descriptor_48_ea8_32s40w_e5_v8?0ls32l8w40l8
- ___67-[MapsSuggestionsXPCActivityTimer scheduleWithTimeInterval:leeway:]_block_invoke.134
- ___block_descriptor_48_ea8_32s40w_e22_v16?0"BGSystemTask"8lw40l8s32l8
- _objc_msgSend$GEOErrorWithCode:userInfo:
- _objc_msgSend$setTaskExpiredWithRetryAfter:error:
Functions:
~ -[MapsSuggestionsXPCActivityTimer initWithName:estimatedDownload:estimatedUpload:queue:block:] : 908 -> 924
~ -[MapsSuggestionsXPCActivityTimer initWithName:queue:timerReturningBlock:] : 1056 -> 1072
~ ___67-[MapsSuggestionsXPCActivityTimer scheduleWithTimeInterval:leeway:]_block_invoke : 1252 -> 1212
~ ___67-[MapsSuggestionsXPCActivityTimer scheduleWithTimeInterval:leeway:]_block_invoke.132 : 1184 -> 1096
~ ___67-[MapsSuggestionsXPCActivityTimer scheduleWithTimeInterval:leeway:]_block_invoke.133 : 228 -> 300
CStrings:
+ "21:11:37"
+ "Apr  8 2026"
+ "Task already completed (expiration handler won the race): %@"
+ "_taskCompleted"
+ "com.apple.maps.suggestions.xpc-activity-execution"
- "21:12:15"
- "GEOErrorWithCode:userInfo:"
- "Mar 23 2026"
- "Task expired before completion"
- "Task expired, requesting retry in 60 seconds: %@"
- "setTaskExpiredWithRetryAfter:error:"

```
