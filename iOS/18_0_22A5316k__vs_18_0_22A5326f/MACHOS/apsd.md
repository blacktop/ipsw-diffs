## apsd

> `/System/Library/PrivateFrameworks/ApplePushService.framework/apsd`

```diff

-1004.100.2.0.0
-  __TEXT.__text: 0xd0804
-  __TEXT.__auth_stubs: 0x25e0
+1006.100.1.0.0
+  __TEXT.__text: 0xd0ad0
+  __TEXT.__auth_stubs: 0x25c0
   __TEXT.__objc_stubs: 0x10160
   __TEXT.__init_offsets: 0x8
-  __TEXT.__objc_methlist: 0xa228
-  __TEXT.__objc_methname: 0x1999f
+  __TEXT.__objc_methlist: 0xa240
+  __TEXT.__objc_methname: 0x199e0
   __TEXT.__objc_classname: 0xfcb
   __TEXT.__objc_methtype: 0x43f0
-  __TEXT.__cstring: 0x9314
+  __TEXT.__cstring: 0x9334
   __TEXT.__const: 0x1c41
-  __TEXT.__oslogstring: 0x11773
+  __TEXT.__oslogstring: 0x117d3
   __TEXT.__gcc_except_tab: 0x24e0
   __TEXT.__dlopen_cstrs: 0xae
   __TEXT.__constg_swiftt: 0x3bc

   __TEXT.__swift5_builtin: 0x14
   __TEXT.__swift5_mpenum: 0x8
   __TEXT.__swift5_proto: 0x10
-  __TEXT.__info_plist: 0xfc
-  __TEXT.__unwind_info: 0x3380
+  __TEXT.__info_plist: 0x3db
+  __TEXT.__unwind_info: 0x3388
   __TEXT.__eh_frame: 0xb0
-  __DATA_CONST.__auth_got: 0x1308
+  __DATA_CONST.__auth_got: 0x12f8
   __DATA_CONST.__got: 0x7c8
   __DATA_CONST.__auth_ptr: 0x98
-  __DATA_CONST.__const: 0x50e8
-  __DATA_CONST.__cfstring: 0x7f80
+  __DATA_CONST.__const: 0x5150
+  __DATA_CONST.__cfstring: 0x7fe0
   __DATA_CONST.__objc_classlist: 0x428
   __DATA_CONST.__objc_protolist: 0x218
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__objc_dictobj: 0xc8
   __DATA_CONST.__objc_arrayobj: 0x30
   __DATA_CONST.__objc_doubleobj: 0x10
-  __DATA.__objc_const: 0x1ebe0
-  __DATA.__objc_selrefs: 0x52e8
-  __DATA.__objc_ivar: 0xd38
+  __DATA.__objc_const: 0x1ec10
+  __DATA.__objc_selrefs: 0x52f8
+  __DATA.__objc_ivar: 0xd3c
   __DATA.__objc_data: 0x3120
   __DATA.__data: 0x18e8
   __DATA.__bss: 0x600

   - /usr/lib/swift/libswiftDispatch.dylib
   - /usr/lib/swift/libswiftObjectiveC.dylib
   - /usr/lib/swift/libswiftXPC.dylib
+  - /usr/lib/swift/libswift_Builtin_float.dylib
+  - /usr/lib/swift/libswift_errno.dylib
+  - /usr/lib/swift/libswift_math.dylib
+  - /usr/lib/swift/libswift_signal.dylib
+  - /usr/lib/swift/libswift_stdio.dylib
+  - /usr/lib/swift/libswift_time.dylib
   - /usr/lib/swift/libswiftos.dylib
-  Functions: 4822
-  Symbols:   900
-  CStrings:  7266
+  - /usr/lib/swift/libswiftsys_time.dylib
+  - /usr/lib/swift/libswiftunistd.dylib
+  Functions: 4825
+  Symbols:   906
+  CStrings:  7274
 
Symbols:
+ _IOPMAssertionCreateWithProperties
+ __swift_FORCE_LOAD_$_swift_Builtin_float
+ __swift_FORCE_LOAD_$_swift_errno
+ __swift_FORCE_LOAD_$_swift_math
+ __swift_FORCE_LOAD_$_swift_signal
+ __swift_FORCE_LOAD_$_swift_stdio
+ __swift_FORCE_LOAD_$_swift_time
+ __swift_FORCE_LOAD_$_swiftsys_time
+ __swift_FORCE_LOAD_$_swiftunistd
- _IOPMAssertionCreateWithDescription
- _OSAtomicDecrement64Barrier
- _OSAtomicIncrement64Barrier
CStrings:
+ "%!@(MISSING) Received a pubsub channel list and client isnt connected on interface %!l(MISSING)d.  Client State: %!l(MISSING)d"
+ "AssertName"
+ "AssertType"
+ "Category"
+ "Ti,N,V_category"
+ "TimeoutSeconds"
+ "_category"
+ "_sendProxyChannelList:onConnectionType:"
+ "category"
+ "setCategory:"
- "TimeoutActionTurnOff"
- "_sendProxyChannelList:"

```
