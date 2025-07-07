## CascadeSets

> `/System/Library/PrivateFrameworks/CascadeSets.framework/CascadeSets`

```diff

-195.0.0.0.0
-  __TEXT.__text: 0x55c0c
-  __TEXT.__auth_stubs: 0xd30
+197.0.0.0.0
+  __TEXT.__text: 0x56168
+  __TEXT.__auth_stubs: 0xd40
   __TEXT.__delay_helper: 0xc8
-  __TEXT.__objc_methlist: 0x48a4
-  __TEXT.__const: 0x3a4
-  __TEXT.__gcc_except_tab: 0x10ac
-  __TEXT.__cstring: 0x3ef2
-  __TEXT.__oslogstring: 0x4d24
+  __TEXT.__objc_methlist: 0x48b4
+  __TEXT.__const: 0x394
+  __TEXT.__gcc_except_tab: 0x10e0
+  __TEXT.__cstring: 0x3ed2
+  __TEXT.__oslogstring: 0x4d14
   __TEXT.__dlopen_cstrs: 0x278
   __TEXT.__swift5_typeref: 0x168
   __TEXT.__swift5_fieldmd: 0xd4
   __TEXT.__constg_swiftt: 0x15c
   __TEXT.__swift5_reflstr: 0x40
-  __TEXT.__swift5_capture: 0xc0
+  __TEXT.__swift5_capture: 0xd0
   __TEXT.__swift5_types: 0x18
   __TEXT.__swift_as_entry: 0x24
   __TEXT.__swift_as_ret: 0x20
   __TEXT.__swift5_protos: 0x4
   __TEXT.__swift5_proto: 0x4
-  __TEXT.__unwind_info: 0x15a8
+  __TEXT.__unwind_info: 0x15e0
   __TEXT.__eh_frame: 0x2f8
   __TEXT.__objc_classname: 0xb3f
-  __TEXT.__objc_methname: 0xa4ce
+  __TEXT.__objc_methname: 0xa50e
   __TEXT.__objc_methtype: 0x1f7e
-  __TEXT.__objc_stubs: 0x6da0
-  __DATA_CONST.__got: 0x4c8
+  __TEXT.__objc_stubs: 0x6de0
+  __DATA_CONST.__got: 0x4d0
   __DATA_CONST.__const: 0x1318
   __DATA_CONST.__objc_classlist: 0x358
   __DATA_CONST.__objc_catlist: 0x20
   __DATA_CONST.__objc_protolist: 0x118
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x24c0
+  __DATA_CONST.__objc_selrefs: 0x24d0
   __DATA_CONST.__objc_protorefs: 0x48
   __DATA_CONST.__objc_superrefs: 0x2c8
   __DATA_CONST.__objc_arraydata: 0x40
-  __AUTH_CONST.__auth_got: 0x6b0
-  __AUTH_CONST.__const: 0x488
+  __AUTH_CONST.__auth_got: 0x6b8
+  __AUTH_CONST.__const: 0x4b0
   __AUTH_CONST.__cfstring: 0x3480
   __AUTH_CONST.__objc_const: 0xaeb0
   __AUTH_CONST.__objc_intobj: 0x420

   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
-  UUID: 41B6F6E7-B5FE-3865-8937-61025C6A9E4A
-  Functions: 2024
-  Symbols:   6675
-  CStrings:  3409
+  UUID: 2424884B-9FC5-3CD5-8916-1E5D52FD5BFC
+  Functions: 2029
+  Symbols:   6686
+  CStrings:  3411
 
Symbols:
+ -[CCDataResourceReadAccess _isDefaultPersonaRequestingUserResource:]
+ -[CCDataResourceReadAccess _shouldEnumerateContainer:]
+ -[CCDataResourceReadAccess _shouldEnumerateContainer:].cold.1
+ -[CCSetChangeXPCEventHandler _setupEventHandlingWithListener:]
+ _BMSetsResource
+ ___46-[CCSetChangeXPCEventHandler _handleXPCEvent:]_block_invoke.11
+ ___46-[CCSetChangeXPCEventHandler _handleXPCEvent:]_block_invoke_2.13
+ ___62-[CCSetChangeXPCEventHandler _setupEventHandlingWithListener:]_block_invoke
+ _block_copy_helper.44
+ _block_descriptor.46
+ _block_destroy_helper.45
+ _objc_msgSend$_isDefaultPersonaRequestingUserResource:
+ _objc_msgSend$_setupEventHandlingWithListener:
+ _objc_msgSend$_shouldEnumerateContainer:
- -[CCDataResourceReadAccess _shouldSkipAccessRequestForResource:]
- ___34-[CCSetChangeXPCEventHandler init]_block_invoke
- ___46-[CCSetChangeXPCEventHandler _handleXPCEvent:]_block_invoke.12
- ___46-[CCSetChangeXPCEventHandler _handleXPCEvent:]_block_invoke_2.14
- _block_copy_helper.39
- _block_descriptor.41
- _block_destroy_helper.40
- _objc_msgSend$_shouldSkipAccessRequestForResource:
CStrings:
+ "%@ adding listener: %@"
+ "%@ firing xpc_event for set: %@"
+ "%@ firing xpc_event returned %d with error %s for set: %@"
+ "%@ removing listener: %@"
+ "%@ setting up xpc_event handling"
+ "<%@ %p> identifier: %@ useCase: %@"
+ "Enumerated %lu readable sets for sets-directory-entitled process with result: %@"
+ "Received xpc_event for set: %@"
+ "Skip enumerating container: %@ as persona: %@"
+ "_isDefaultPersonaRequestingUserResource:"
+ "_setupEventHandlingWithListener:"
+ "_shouldEnumerateContainer:"
- "<%@ %p> identifier: %@"
- "CCSetChangeXPCEventHandler adding listener: %@"
- "CCSetChangeXPCEventHandler removing listener: %@"
- "CCSetChangeXPCEventHandler setting up XPC event handler"
- "CCSetChangeXPCNotifier firing xpc_event"
- "CCSetChangeXPCNotifier firing xpc_event returned %d with errno %d"
- "Enumerated %lu readable sets for internal process with result: %@"
- "Handling xpc_event"
- "_shouldSkipAccessRequestForResource:"
- "com.apple.cascade.setChange.xpc.eventHandler"

```
