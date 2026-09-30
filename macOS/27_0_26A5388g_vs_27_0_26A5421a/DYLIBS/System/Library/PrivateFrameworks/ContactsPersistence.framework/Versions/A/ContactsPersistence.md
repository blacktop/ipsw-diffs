## ContactsPersistence

> `/System/Library/PrivateFrameworks/ContactsPersistence.framework/Versions/A/ContactsPersistence`

```diff

-3839.100.3.0.0
-  __TEXT.__text: 0x5027c
-  __TEXT.__objc_methlist: 0x528c
+3844.100.1.0.0
+  __TEXT.__text: 0x505cc
+  __TEXT.__objc_methlist: 0x534c
   __TEXT.__const: 0xcd8
-  __TEXT.__cstring: 0x30bf
+  __TEXT.__cstring: 0x30ef
   __TEXT.__oslogstring: 0x335a
-  __TEXT.__gcc_except_tab: 0x6a4
+  __TEXT.__gcc_except_tab: 0x6e4
   __TEXT.__constg_swiftt: 0x86c
   __TEXT.__swift5_typeref: 0x537
   __TEXT.__swift5_reflstr: 0x1a3

   __TEXT.__swift5_types: 0x54
   __TEXT.__swift5_protos: 0xc
   __TEXT.__swift5_capture: 0x60
-  __TEXT.__unwind_info: 0x1700
+  __TEXT.__unwind_info: 0x1710
   __TEXT.__eh_frame: 0xc8
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0

   __DATA_CONST.__const: 0x1008
   __DATA_CONST.__objc_classlist: 0x4d8
   __DATA_CONST.__objc_catlist: 0x30
-  __DATA_CONST.__objc_protolist: 0x100
+  __DATA_CONST.__objc_protolist: 0x108
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x3240
+  __DATA_CONST.__objc_selrefs: 0x32b0
   __DATA_CONST.__objc_protorefs: 0x50
   __DATA_CONST.__objc_superrefs: 0x210
   __DATA_CONST.__objc_arraydata: 0x88
-  __DATA_CONST.__got: 0x870
-  __AUTH_CONST.__const: 0x1ff0
-  __AUTH_CONST.__cfstring: 0x4020
-  __AUTH_CONST.__objc_const: 0xb5a8
+  __DATA_CONST.__got: 0x878
+  __AUTH_CONST.__const: 0x2050
+  __AUTH_CONST.__cfstring: 0x4060
+  __AUTH_CONST.__objc_const: 0xb620
   __AUTH_CONST.__objc_arrayobj: 0x60
   __AUTH_CONST.__objc_intobj: 0xa8
   __AUTH_CONST.__auth_got: 0x798
   __AUTH.__objc_data: 0x1d90
   __AUTH.__data: 0x5a0
   __DATA.__objc_ivar: 0x408
-  __DATA.__data: 0xe80
+  __DATA.__data: 0xee0
   __DATA.__bss: 0xf00
   __DATA.__common: 0x40
   __DATA_DIRTY.__objc_data: 0x1810

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 2322
-  Symbols:   5489
-  CStrings:  847
+  Functions: 2327
+  Symbols:   5505
+  CStrings:  849
 
Symbols:
+ -[CNCDRemotePersistentStoreEndpointFactory _fetchEndpoint]
+ -[CNCDRemotePersistentStoreEndpointFactory maximumNumberOfAttemptsForRetry:]
+ -[CNCDRemotePersistentStoreEndpointFactory retry:delayAfterError:onAttempt:]
+ -[CNCDRemotePersistentStoreEndpointFactory retry:shouldContinueAfterError:onAttempt:]
+ _OBJC_CLASS_$_CNRetry
+ __58-[CNCDRemotePersistentStoreEndpointFactory _fetchEndpoint]_block_invoke
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_CNRetryDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CNRetryDelegate
+ __OBJC_$_PROTOCOL_REFS_CNRetryDelegate
+ __OBJC_LABEL_PROTOCOL_$_CNRetryDelegate
+ __OBJC_PROTOCOL_$_CNRetryDelegate
+ ___58-[CNCDRemotePersistentStoreEndpointFactory _fetchEndpoint]_block_invoke
+ ___block_descriptor_40_e8_32s_e15_"CNResult"8?0l
+ ___block_descriptor_48_e8_32s40r_e17_v16?0"NSError"8l
+ _objc_msgSend$_fetchEndpoint
+ _objc_msgSend$initWithDelegate:
+ _objc_msgSend$performAndWait:
- __65-[CNCDRemotePersistentStoreEndpointFactory newEndpointWithError:]_block_invoke
CStrings:
+ "CNErrorDomain"
+ "Unknown XPC connection failure"
```
