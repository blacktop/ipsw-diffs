## FindMyDevice

> `/System/Library/PrivateFrameworks/FindMyDevice.framework/FindMyDevice`

```diff

-455.35.2.23.3
-  __TEXT.__text: 0x23184
-  __TEXT.__auth_stubs: 0x410
+455.35.2.23.5
+  __TEXT.__text: 0x2317c
+  __TEXT.__auth_stubs: 0x430
   __TEXT.__objc_methlist: 0x289c
   __TEXT.__const: 0xb8
   __TEXT.__oslogstring: 0x2af1
   __TEXT.__cstring: 0x415f
-  __TEXT.__gcc_except_tab: 0x2f0
-  __TEXT.__unwind_info: 0xa10
+  __TEXT.__gcc_except_tab: 0x2e0
+  __TEXT.__unwind_info: 0xa18
   __TEXT.__objc_classname: 0x6a2
-  __TEXT.__objc_methname: 0x51e6
-  __TEXT.__objc_methtype: 0x11ef
-  __TEXT.__objc_stubs: 0x37c0
+  __TEXT.__objc_methname: 0x51f6
+  __TEXT.__objc_methtype: 0x121c
+  __TEXT.__objc_stubs: 0x3760
   __DATA_CONST.__got: 0x188
   __DATA_CONST.__const: 0x1200
   __DATA_CONST.__objc_classlist: 0x150

   __DATA_CONST.__objc_selrefs: 0x12e8
   __DATA_CONST.__objc_protorefs: 0x68
   __DATA_CONST.__objc_superrefs: 0x118
-  __AUTH_CONST.__auth_got: 0x218
+  __AUTH_CONST.__auth_got: 0x228
   __AUTH_CONST.__const: 0x500
   __AUTH_CONST.__cfstring: 0x3d20
-  __AUTH_CONST.__objc_const: 0x7788
+  __AUTH_CONST.__objc_const: 0x77a8
   __AUTH_CONST.__objc_intobj: 0x18
   __AUTH.__objc_data: 0x7d0
-  __DATA.__objc_ivar: 0x22c
+  __DATA.__objc_ivar: 0x230
   __DATA.__data: 0x970
   __DATA.__bss: 0x128
   __DATA.__common: 0x8

   - /System/Library/PrivateFrameworks/InternationalSupport.framework/InternationalSupport
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 767837A9-737D-34FA-A63F-83C794260213
+  UUID: 241A594E-5ADD-3F95-9943-7E785D86884A
   Functions: 1022
   Symbols:   4086
-  CStrings:  2445
+  CStrings:  2447
 
Symbols:
+ _OBJC_IVAR_$_FMNSXPCConnection._connectionLock
+ _os_unfair_lock_lock
+ _os_unfair_lock_unlock
- _objc_msgSend$_cachedRemoteObjectProxy
- _objc_msgSend$_testMockConnection
- _objc_msgSend$set_cachedRemoteObjectProxy:
Functions:
~ -[FMNSXPCConnection initWithConfiguration:exportedObject:] : 908 -> 912
~ -[FMNSXPCConnection remoteObjectProxy] : 348 -> 340
~ -[FMNSXPCConnection state] : 88 -> 84
CStrings:
+ "_connectionLock"
+ "{os_unfair_lock_s=\"_os_unfair_lock_opaque\"I}"

```
