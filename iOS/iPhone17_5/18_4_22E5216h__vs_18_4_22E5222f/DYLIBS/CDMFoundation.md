## CDMFoundation

> `/System/Library/PrivateFrameworks/CDMFoundation.framework/CDMFoundation`

```diff

-3404.67.6.1.2
-  __TEXT.__text: 0x25563c
-  __TEXT.__auth_stubs: 0x9600
-  __TEXT.__objc_methlist: 0x7e74
-  __TEXT.__const: 0xa807
-  __TEXT.__swift5_typeref: 0x3e20
-  __TEXT.__swift5_fieldmd: 0x3920
-  __TEXT.__constg_swiftt: 0x517c
+3404.75.1.0.0
+  __TEXT.__text: 0x2565b8
+  __TEXT.__auth_stubs: 0x9630
+  __TEXT.__objc_methlist: 0x7e9c
+  __TEXT.__const: 0xa83f
+  __TEXT.__swift5_typeref: 0x3e3e
+  __TEXT.__swift5_fieldmd: 0x3948
+  __TEXT.__constg_swiftt: 0x5198
   __TEXT.__swift5_protos: 0x94
-  __TEXT.__cstring: 0x1bb1d
-  __TEXT.__swift5_types: 0x514
+  __TEXT.__cstring: 0x1bbf5
+  __TEXT.__swift5_types: 0x518
   __TEXT.__swift5_reflstr: 0x2c7e
-  __TEXT.__oslogstring: 0x1bb58
-  __TEXT.__swift5_proto: 0x910
+  __TEXT.__oslogstring: 0x1bd58
+  __TEXT.__swift5_proto: 0x914
   __TEXT.__swift5_assocty: 0x438
   __TEXT.__swift5_capture: 0xbd8
   __TEXT.__swift5_builtin: 0xf0
   __TEXT.__swift5_mpenum: 0x3c
   __TEXT.__swift_as_entry: 0x218
   __TEXT.__swift_as_ret: 0x260
-  __TEXT.__gcc_except_tab: 0xc55c
+  __TEXT.__gcc_except_tab: 0xc5a0
   __TEXT.__ustring: 0x164
-  __TEXT.__unwind_info: 0x79a8
-  __TEXT.__eh_frame: 0x791c
+  __TEXT.__unwind_info: 0x79d8
+  __TEXT.__eh_frame: 0x7944
   __TEXT.__objc_classname: 0x15a7
-  __TEXT.__objc_methname: 0x161e1
-  __TEXT.__objc_methtype: 0x32d6
-  __TEXT.__objc_stubs: 0xfec0
-  __DATA_CONST.__got: 0x2628
+  __TEXT.__objc_methname: 0x1624e
+  __TEXT.__objc_methtype: 0x32e5
+  __TEXT.__objc_stubs: 0xff20
+  __DATA_CONST.__got: 0x2660
   __DATA_CONST.__const: 0x1dc8
   __DATA_CONST.__objc_classlist: 0x8b0
   __DATA_CONST.__objc_catlist: 0x50
   __DATA_CONST.__objc_protolist: 0x140
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x4fe8
+  __DATA_CONST.__objc_selrefs: 0x5000
   __DATA_CONST.__objc_protorefs: 0x80
   __DATA_CONST.__objc_superrefs: 0x3f8
   __DATA_CONST.__objc_arraydata: 0x60
-  __AUTH_CONST.__auth_got: 0x4b18
-  __AUTH_CONST.__auth_ptr: 0x1270
-  __AUTH_CONST.__const: 0x95b0
+  __AUTH_CONST.__auth_got: 0x4b30
+  __AUTH_CONST.__auth_ptr: 0x11d8
+  __AUTH_CONST.__const: 0x9600
   __AUTH_CONST.__cfstring: 0x7d20
   __AUTH_CONST.__objc_const: 0x11cd0
   __AUTH_CONST.__objc_arrayobj: 0x30

   __AUTH_CONST.__objc_doubleobj: 0x10
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH.__objc_data: 0x1ff0
-  __AUTH.__data: 0x4398
+  __AUTH.__data: 0x43a8
   __DATA.__objc_ivar: 0x740
-  __DATA.__data: 0x3020
-  __DATA.__bss: 0xf9b0
+  __DATA.__data: 0x3040
+  __DATA.__bss: 0xf9c0
   __DATA.__common: 0x7a0
   __DATA_DIRTY.__objc_data: 0x3af8
   __DATA_DIRTY.__data: 0x438

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 11070
-  Symbols:   8320
-  CStrings:  8445
+  Functions: 11086
+  Symbols:   8336
+  CStrings:  8454
 
Symbols:
+ _dispatch_after
CStrings:
+ "%s [ERR]: The call to [VCVoiceShortcutClient getVoiceShortcutsWithCompletion] failed to invoke the completion block before the %fs timeout. To avoid a transaction leak, the `fetchVoiceShortcutsWithMatcher` transaction will be manually closed. This has the effect of aborting voice shortcuts handling if the completion block is called afterwards."
+ "%s [WARN]: The `fetchVoiceShortcutsWithMatcher` transaction is nil. This means that we hit the %fs timeout before the completion block was called. Aborting handling."
+ "+[CDMSSUService(SystemEvent) fetchVoiceShortcutsWithMatcher:assetCollection:block:]_block_invoke"
+ "+[CDMSSUService(SystemEvent) handleFetchVoiceShortcutsTimeout:transactionPtr:]"
+ "com.apple.siri.cdm.CDMSSUServiceTimeout"
+ "getCompletionBlockTimeoutSeconds"
+ "getSystemEventTimeoutQueue"
+ "handleFetchVoiceShortcutsTimeout:transactionPtr:"
+ "v32@0:8d16^@24"

```
