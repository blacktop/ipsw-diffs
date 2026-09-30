## libramrod.dylib

> `/usr/lib/libramrod.dylib`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__const`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__AUTH_CONST.__objc_const`
- `__AUTH_CONST.__objc_intobj`
- `__AUTH.__objc_data`
- `__AUTH.__data`
- `__DATA.__objc_classrefs`
- `__DATA.__objc_superrefs`
- `__DATA.__data`

```diff

 3696.0.12.0.3
-  __TEXT.__text: 0xeedb4
+  __TEXT.__text: 0xf0a70
   __TEXT.__objc_methlist: 0x119c
-  __TEXT.__cstring: 0x2bbc5
+  __TEXT.__cstring: 0x2be81
   __TEXT.__const: 0x79110
-  __TEXT.__gcc_except_tab: 0xb2c
-  __TEXT.__oslogstring: 0xac8
-  __TEXT.__unwind_info: 0x1e88
-  __TEXT.__eh_frame: 0x378
-  __TEXT.__objc_stubs: 0x2900
-  __TEXT.__auth_stubs: 0x2af0
+  __TEXT.__gcc_except_tab: 0xb6c
+  __TEXT.__oslogstring: 0xb92
+  __TEXT.__unwind_info: 0x1eb0
+  __TEXT.__eh_frame: 0x380
+  __TEXT.__objc_stubs: 0x2920
+  __TEXT.__auth_stubs: 0x2b40
   __TEXT.__objc_classname: 0x18b
-  __TEXT.__objc_methname: 0x29f1
+  __TEXT.__objc_methname: 0x29fe
   __TEXT.__objc_methtype: 0xb58
   __DATA_CONST.__const: 0x1f88
   __DATA_CONST.__objc_classlist: 0x90
   __DATA_CONST.__objc_protolist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__weak_got: 0x8
-  __DATA_CONST.__objc_selrefs: 0xcd0
+  __DATA_CONST.__objc_selrefs: 0xcd8
   __DATA_CONST.__got: 0x2c0
-  __AUTH_CONST.__const: 0x2068
-  __AUTH_CONST.__cfstring: 0xc3c0
+  __AUTH_CONST.__const: 0x20b8
+  __AUTH_CONST.__cfstring: 0xc480
   __AUTH_CONST.__objc_const: 0x1ad0
   __AUTH_CONST.__weak_auth_got: 0x10
   __AUTH_CONST.__objc_intobj: 0x30
-  __AUTH_CONST.__auth_got: 0x1580
+  __AUTH_CONST.__auth_got: 0x15a8
   __AUTH.__objc_data: 0x5a0
   __AUTH.__data: 0x318
   __DATA.__objc_classrefs: 0x128

   - /usr/lib/libz.1.dylib
   - /usr/lib/updaters/libAppleTypeCRetimerUpdater.dylib
   - /usr/lib/updaters/libBMCMCUUpdater.dylib
-  Functions: 2862
-  Symbols:   1886
-  CStrings:  6360
+  Functions: 2871
+  Symbols:   1892
+  CStrings:  6386
 
Symbols:
+ __ramrod_device_supports_provisional_nonce_rollback
+ _notify_cancel
+ _notify_get_state
+ _notify_post
+ _notify_register_check
+ _notify_register_dispatch
CStrings:
+ "%@/bic_sec"
+ "%@/genx_history"
+ "%@/history_sec"
+ "--set-provisional"
+ "--slot"
+ "ApplePearlExclaveSEPDriver"
+ "Generating reference frames info record...\n"
+ "IODeviceTree:/product/display%d"
+ "Reference frames info record written to %s\n"
+ "ReferenceFramesSetInfo, index: %zu, type: %d, count: %d, size: %d\n"
+ "Verifying new reference frames info record...\n"
+ "com.apple.pearld.check_secure_streaming"
+ "com.apple.pearld.ready"
+ "ctx[%d]: display \"%s\" (display index %d)\n"
+ "display%d: display-boot-rotation = %u\n"
+ "display%d: display-rotation = %u\n"
+ "display-boot-rotation"
+ "display-rotation"
+ "mutableBytes"
+ "notifyResult == 0"
+ "outDataSize <= signedRefFramesInfoRecordData.length"
+ "pearldReady"
+ "reference-info-record.DAT"
+ "requestData"
+ "sema"
+ "signedRefFramesInfoRecordData"
```
