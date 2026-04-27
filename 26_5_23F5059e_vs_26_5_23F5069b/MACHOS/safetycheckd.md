## safetycheckd

> `/usr/libexec/safetycheckd`

```diff

-616.0.1.0.1
-  __TEXT.__text: 0x8c90
-  __TEXT.__auth_stubs: 0x4e0
+616.2.0.0.0
+  __TEXT.__text: 0x944c
+  __TEXT.__auth_stubs: 0x500
   __TEXT.__objc_stubs: 0xe80
-  __TEXT.__objc_methlist: 0x500
-  __TEXT.__const: 0x58
-  __TEXT.__objc_methname: 0xe49
-  __TEXT.__oslogstring: 0xb5c
-  __TEXT.__objc_classname: 0xe8
+  __TEXT.__objc_methlist: 0x518
+  __TEXT.__const: 0x60
+  __TEXT.__objc_methname: 0xee8
+  __TEXT.__oslogstring: 0xbba
+  __TEXT.__objc_classname: 0xea
   __TEXT.__objc_methtype: 0x322
-  __TEXT.__cstring: 0x394
-  __TEXT.__gcc_except_tab: 0x574
+  __TEXT.__cstring: 0x3c6
+  __TEXT.__gcc_except_tab: 0x584
   __TEXT.__unwind_info: 0x220
-  __DATA_CONST.__auth_got: 0x280
+  __DATA_CONST.__auth_got: 0x290
   __DATA_CONST.__got: 0x160
   __DATA_CONST.__auth_ptr: 0x8
-  __DATA_CONST.__const: 0x3c8
+  __DATA_CONST.__const: 0x3f0
   __DATA_CONST.__cfstring: 0x220
   __DATA_CONST.__objc_classlist: 0x28
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x28
-  __DATA.__objc_const: 0x870
-  __DATA.__objc_selrefs: 0x478
-  __DATA.__objc_ivar: 0x3c
+  __DATA.__objc_const: 0x8a0
+  __DATA.__objc_selrefs: 0x488
+  __DATA.__objc_ivar: 0x40
   __DATA.__objc_data: 0x190
   __DATA.__data: 0x248
   __DATA.__bss: 0x38

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/liblockdown.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 4506F9F1-D7CA-3BD2-902E-86D4A2DBAE2A
-  Functions: 122
-  Symbols:   132
-  CStrings:  358
+  UUID: 76554F4C-82D9-34C1-B629-228E7A328777
+  Functions: 126
+  Symbols:   134
+  CStrings:  364
 
Symbols:
+ __dispatch_source_type_timer
+ _dispatch_resume
+ _dispatch_source_cancel
+ _dispatch_source_create
+ _dispatch_source_set_event_handler
+ _dispatch_source_set_timer
- __dispatch_main_q
- _dispatch_semaphore_create
- _dispatch_semaphore_signal
- _dispatch_semaphore_wait
CStrings:
+ "Failed to fetch shared resources from %{public}@ because exception %{public}@ (after timeout)"
+ "T@\"NSObject<OS_dispatch_queue>\",&,N,V_fetchSharingPermissionsQueue"
+ "_fetchSharingPermissionsQueue"
+ "com.apple.safetycheckd.SCDaemonService.replyQueue"
+ "fetchSharingPermissionsQueue"
+ "setFetchSharingPermissionsQueue:"

```
