## IOMFB_bics_daemon

> `/usr/libexec/IOMFB_bics_daemon`

```diff

-  __TEXT.__text: 0x2f354
+  __TEXT.__text: 0x30868
   __TEXT.__auth_stubs: 0x1370
   __TEXT.__objc_stubs: 0x140
   __TEXT.__objc_methlist: 0x5c
-  __TEXT.__cstring: 0x4dac
-  __TEXT.__const: 0x5064
-  __TEXT.__gcc_except_tab: 0xaf0
+  __TEXT.__cstring: 0x51fc
+  __TEXT.__const: 0x5cf4
+  __TEXT.__gcc_except_tab: 0xb5c
   __TEXT.__objc_methname: 0xdf
   __TEXT.__objc_classname: 0x2a
   __TEXT.__objc_methtype: 0xb0
   __TEXT.__swift5_typeref: 0x904
-  __TEXT.__swift5_reflstr: 0x248
+  __TEXT.__swift5_reflstr: 0x268
   __TEXT.__swift5_assocty: 0x350
   __TEXT.__constg_swiftt: 0xa94
-  __TEXT.__swift5_fieldmd: 0x38c
+  __TEXT.__swift5_fieldmd: 0x3b0
   __TEXT.__swift5_builtin: 0x50
   __TEXT.__swift5_proto: 0x84
   __TEXT.__swift5_types: 0x38
   __TEXT.__swift5_protos: 0x50
   __TEXT.__swift5_types2: 0x4
-  __TEXT.__unwind_info: 0xcd8
-  __TEXT.__eh_frame: 0xc40
-  __DATA_CONST.__const: 0xee0
+  __TEXT.__unwind_info: 0xd18
+  __TEXT.__eh_frame: 0xd48
+  __DATA_CONST.__const: 0xf90
   __DATA_CONST.__cfstring: 0x280
   __DATA_CONST.__objc_classlist: 0x10
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA.__objc_selrefs: 0x58
   __DATA.__objc_ivar: 0x18
   __DATA.__objc_data: 0xa0
-  __DATA.__data: 0xbc8
+  __DATA.__data: 0xb80
   __DATA.__bss: 0x16a0
   __DATA.__common: 0x28
   - /System/Library/Frameworks/Accelerate.framework/Accelerate

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 962
+  Functions: 978
   Symbols:   511
-  CStrings:  757
+  CStrings:  783
 
Sections:
~ __TEXT.__objc_methlist : content changed
~ __TEXT.__swift5_typeref : content changed
~ __TEXT.__swift5_assocty : content changed
~ __TEXT.__constg_swiftt : content changed
~ __TEXT.__swift5_builtin : content changed
~ __TEXT.__swift5_proto : content changed
~ __TEXT.__swift5_types : content changed
~ __TEXT.__swift5_protos : content changed
~ __TEXT.__swift5_types2 : content changed
~ __DATA_CONST.__cfstring : content changed
~ __DATA_CONST.__auth_got : content changed
~ __DATA_CONST.__got : content changed
~ __DATA_CONST.__auth_ptr : content changed
~ __DATA.__objc_const : content changed
~ __DATA.__objc_selrefs : content changed
Symbols:
+ _CFRunLoopTimerInvalidate
+ _exp
- __ZdaPvSt19__type_descriptor_t
- __ZnamSt19__type_descriptor_t
CStrings:
+ "%s saving genx history "
+ "%s: %s file not found, skipping"
+ "%s: concatenated storage is full"
+ "%s: could not allocate enough memory, skipping"
+ "%s: could not stat genx history file, skipping"
+ "%s: failed to read genx history data"
+ "%s: invalid buffer ptr"
+ "%s: invalid concatenated storage header in buffer"
+ "GenX disabled, canceling timer\n"
+ "GenX: backup history storage is not in correct format"
+ "GenX: backup storage is not in correct format"
+ "GenX: ean data too small for concatenated storage"
+ "GenX: ean handle not available for backup history read"
+ "GenX: error with backup history buffer"
+ "GenX: failed to read history from backup: 0x%x"
+ "GenX: failed to upload calibration ACSS matrix %s"
+ "GenX: failed to upload calibration data, disabling GenX"
+ "GenX: failed to upload calibration temperature %s"
+ "GenX: failing to initialize Aref and beta %s skip fitting"
+ "GenX: genx history file is invalid, trying backup history"
+ "GenX: invalid GenX data size in concatenated storage"
+ "GenX: no backup history found in ean"
+ "GenX: no genx history file, trying backup history"
+ "GenX: reading history from storage backup"
+ "GenX: successfully restored history from storage backup"
+ "Invalid buffer"
+ "Not Privileged"
+ "backup genx history"
+ "save_genx_backup"
- " no genx history file "
- "GenX: failed to upload calibration data %s, disabling GenX"
- "diagnostics"

```
