## ContactsPersistence

> `/System/Library/PrivateFrameworks/ContactsPersistence.framework/ContactsPersistence`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_typeref`
- `__TEXT.__swift5_proto`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH.__objc_data`
- `__AUTH.__data`

```diff

-3839.100.3.2.1
-  __TEXT.__text: 0x4a9e0
-  __TEXT.__objc_methlist: 0x522c
+3844.100.1.0.0
+  __TEXT.__text: 0x4ad04
+  __TEXT.__objc_methlist: 0x52ec
   __TEXT.__const: 0xca8
-  __TEXT.__cstring: 0x306f
+  __TEXT.__cstring: 0x308f
   __TEXT.__oslogstring: 0x32ca
-  __TEXT.__gcc_except_tab: 0x634
+  __TEXT.__gcc_except_tab: 0x674
   __TEXT.__constg_swiftt: 0x86c
   __TEXT.__swift5_typeref: 0x537
   __TEXT.__swift5_reflstr: 0x1a3

   __TEXT.__swift5_types: 0x54
   __TEXT.__swift5_protos: 0xc
   __TEXT.__swift5_capture: 0x60
-  __TEXT.__unwind_info: 0x15e8
+  __TEXT.__unwind_info: 0x15f8
   __TEXT.__eh_frame: 0x148
   __TEXT.__objc_stubs: 0x0
   __TEXT.__auth_stubs: 0x0
   __TEXT.__objc_classname: 0x0
   __TEXT.__objc_methname: 0x0
   __TEXT.__objc_methtype: 0x0
-  __DATA_CONST.__const: 0x1c08
+  __DATA_CONST.__const: 0x1c58
   __DATA_CONST.__objc_classlist: 0x4d0
   __DATA_CONST.__objc_catlist: 0x30
-  __DATA_CONST.__objc_protolist: 0x100
+  __DATA_CONST.__objc_protolist: 0x108
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x31f0
+  __DATA_CONST.__objc_selrefs: 0x3260
   __DATA_CONST.__objc_protorefs: 0x50
   __DATA_CONST.__objc_superrefs: 0x210
   __DATA_CONST.__objc_arraydata: 0x88
-  __DATA_CONST.__got: 0x828
+  __DATA_CONST.__got: 0x830
   __AUTH_CONST.__const: 0x11a0
-  __AUTH_CONST.__cfstring: 0x4020
-  __AUTH_CONST.__objc_const: 0xb4b8
+  __AUTH_CONST.__cfstring: 0x4060
+  __AUTH_CONST.__objc_const: 0xb530
   __AUTH_CONST.__objc_arrayobj: 0x60
   __AUTH_CONST.__objc_intobj: 0xa8
   __AUTH_CONST.__auth_got: 0x8d8
   __AUTH.__objc_data: 0x3550
   __AUTH.__data: 0x5a0
   __DATA.__objc_ivar: 0x408
-  __DATA.__data: 0xe58
+  __DATA.__data: 0xeb8
   __DATA.__bss: 0x1130
   __DATA.__common: 0x48
   - /System/Library/Frameworks/Accounts.framework/Accounts

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 2265
-  Symbols:   5419
-  CStrings:  843
+  Functions: 2270
+  Symbols:   5435
+  CStrings:  845
 
Symbols:
+ -[CNCDRemotePersistentStoreEndpointFactory _fetchEndpoint]
+ -[CNCDRemotePersistentStoreEndpointFactory maximumNumberOfAttemptsForRetry:]
+ -[CNCDRemotePersistentStoreEndpointFactory retry:delayAfterError:onAttempt:]
+ -[CNCDRemotePersistentStoreEndpointFactory retry:shouldContinueAfterError:onAttempt:]
+ _OBJC_CLASS_$_CNRetry
+ __OBJC_$_PROTOCOL_INSTANCE_METHODS_OPT_CNRetryDelegate
+ __OBJC_$_PROTOCOL_METHOD_TYPES_CNRetryDelegate
+ __OBJC_$_PROTOCOL_REFS_CNRetryDelegate
+ __OBJC_LABEL_PROTOCOL_$_CNRetryDelegate
+ __OBJC_PROTOCOL_$_CNRetryDelegate
+ ___58-[CNCDRemotePersistentStoreEndpointFactory _fetchEndpoint]_block_invoke
+ ___block_descriptor_40_e8_32s_e15_"CNResult"8?0ls32l8
+ ___block_descriptor_48_e8_32s40r_e17_v16?0"NSError"8lr40l8s32l8
+ _objc_msgSend$_fetchEndpoint
+ _objc_msgSend$initWithDelegate:
+ _objc_msgSend$performAndWait:
CStrings:
+ "CNErrorDomain"
+ "Unknown XPC connection failure"
```
