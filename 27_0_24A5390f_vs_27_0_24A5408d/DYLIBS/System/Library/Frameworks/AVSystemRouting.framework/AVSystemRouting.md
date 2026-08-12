## AVSystemRouting

> `/System/Library/Frameworks/AVSystemRouting.framework/AVSystemRouting`

### Sections with Same Size but Changed Content

- `__TEXT.__cstring`

```diff

-360.70.2.0.0
-  __TEXT.__text: 0x22fdc
-  __TEXT.__objc_methlist: 0xdcc
+360.75.1.1.0
+  __TEXT.__text: 0x2326c
+  __TEXT.__objc_methlist: 0xdec
   __TEXT.__const: 0x19d8
-  __TEXT.__gcc_except_tab: 0x288
+  __TEXT.__gcc_except_tab: 0x2cc
   __TEXT.__cstring: 0xc8a
-  __TEXT.__oslogstring: 0x634
+  __TEXT.__oslogstring: 0x6a4
   __TEXT.__swift5_typeref: 0x77c
   __TEXT.__swift5_capture: 0x960
   __TEXT.__constg_swiftt: 0xa48

   __TEXT.__swift_as_entry: 0xc4
   __TEXT.__swift_as_ret: 0x44
   __TEXT.__swift_as_cont: 0xbc
-  __TEXT.__unwind_info: 0xd30
+  __TEXT.__unwind_info: 0xd48
   __TEXT.__eh_frame: 0x14d8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __DATA_CONST.__objc_classlist: 0xa0
   __DATA_CONST.__objc_protolist: 0xb0
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x7c0
+  __DATA_CONST.__objc_selrefs: 0x7d8
   __DATA_CONST.__objc_protorefs: 0x48
   __DATA_CONST.__objc_superrefs: 0x48
   __DATA_CONST.__got: 0x228
   __AUTH_CONST.__const: 0x14e0
   __AUTH_CONST.__cfstring: 0x9c0
-  __AUTH_CONST.__objc_const: 0x2278
+  __AUTH_CONST.__objc_const: 0x2298
   __AUTH_CONST.__auth_got: 0x710
   __AUTH.__objc_data: 0x470
   __AUTH.__data: 0xc50
-  __DATA.__objc_ivar: 0xb8
+  __DATA.__objc_ivar: 0xbc
   __DATA.__data: 0x670
   __DATA.__common: 0x20
   __DATA.__bss: 0xce0

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 1081
-  Symbols:   1144
-  CStrings:  137
+  Functions: 1082
+  Symbols:   1151
+  CStrings:  138
 
Symbols:
+ -[AVSystemRoute _removeFailedSession:]
+ -[AVSystemRouteSession setRoute:]
+ GCC_except_table10
+ GCC_except_table21
+ GCC_except_table22
+ GCC_except_table30
+ GCC_except_table31
+ GCC_except_table34
+ GCC_except_table38
+ GCC_except_table44
+ _OBJC_IVAR_$_AVSystemRouteSession._route
+ _objc_msgSend$_removeFailedSession:
+ _objc_msgSend$onlySupportsRealtimeAudio
+ _objc_msgSend$setRoute:
- GCC_except_table19
- GCC_except_table26
- GCC_except_table27
- GCC_except_table32
- GCC_except_table36
- GCC_except_table42
- _OUTLINED_FUNCTION_24
Functions:
~ -[AVSystemRoute addSession:] : 172 -> 184
~ -[AVSystemRoute removeSession:] : 156 -> 168
+ -[AVSystemRoute _removeFailedSession:]
+ -[AVSystemRouteSession setRoute:]
~ ___51-[AVSystemRouteSession startWithCompletionHandler:]_block_invoke : 104 -> 220
~ -[AVSystemRouteSession .cxx_destruct] : 8 -> 60
~ _OUTLINED_FUNCTION_5 : 32 -> 16
~ _OUTLINED_FUNCTION_6 : 16 -> 20
~ _OUTLINED_FUNCTION_7 : 12 -> 32
~ _OUTLINED_FUNCTION_8 : 12 -> 44
~ _OUTLINED_FUNCTION_9 : 20 -> 32
~ _OUTLINED_FUNCTION_11 : 44 -> 12
~ _OUTLINED_FUNCTION_12 : 28 -> 12
~ _OUTLINED_FUNCTION_13 : 16 -> 32
~ _OUTLINED_FUNCTION_14 : 16 -> 44
~ _OUTLINED_FUNCTION_15 : 28 -> 16
~ _OUTLINED_FUNCTION_16 : 36 -> 16
~ _OUTLINED_FUNCTION_17 : 24 -> 12
~ _OUTLINED_FUNCTION_18 : 12 -> 28
~ _OUTLINED_FUNCTION_19 : 20 -> 36
~ _OUTLINED_FUNCTION_20 : 12 -> 24
~ _OUTLINED_FUNCTION_21 : 12 -> 20
~ _OUTLINED_FUNCTION_22 : 32 -> 12
- _OUTLINED_FUNCTION_24
~ -[AVCustomRoutingSystemControllerSystemCastingImpl _handleMediaServicesReset] : 260 -> 256
~ -[AVCustomRoutingSystemControllerSystemCastingImpl _updateSystemRoutingState] : 1516 -> 1780
~ -[AVCustomRoutingSystemControllerSystemCastingImpl stopApplication] : 204 -> 200
CStrings:
+ "-AVCustomRoutingSystemController- %s: All custom protocol devices only support Real-Time Audio. Skipping event."
+ "B"
- "A"
```
