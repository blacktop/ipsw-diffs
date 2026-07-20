## meminfo

> `/usr/bin/meminfo`

### Sections with Same Size but Changed Content

- `__TEXT.__swift5_entry`
- `__TEXT.__swift5_builtin`
- `__TEXT.__swift5_protos`
- `__DATA.__objc_selrefs`

```diff

-1070.0.0.0.0
-  __TEXT.__text: 0xfe78
-  __TEXT.__auth_stubs: 0x970
+1071.0.1.0.0
+  __TEXT.__text: 0x138a0
+  __TEXT.__auth_stubs: 0x9c0
   __TEXT.__objc_stubs: 0x100
-  __TEXT.__const: 0x784
+  __TEXT.__const: 0x9b4
   __TEXT.__swift5_entry: 0x8
-  __TEXT.__swift5_typeref: 0x222
-  __TEXT.__constg_swiftt: 0x1c0
-  __TEXT.__swift5_reflstr: 0x23a
-  __TEXT.__swift5_fieldmd: 0x444
-  __TEXT.__cstring: 0x899
+  __TEXT.__swift5_typeref: 0x2b2
+  __TEXT.__constg_swiftt: 0x214
+  __TEXT.__swift5_reflstr: 0x29c
+  __TEXT.__swift5_fieldmd: 0x510
+  __TEXT.__cstring: 0x7f4
   __TEXT.__swift5_builtin: 0x14
-  __TEXT.__swift5_proto: 0x38
-  __TEXT.__swift5_types: 0x2c
+  __TEXT.__swift5_proto: 0x40
+  __TEXT.__swift5_types: 0x38
   __TEXT.__swift5_protos: 0x4
   __TEXT.__objc_methname: 0x98
-  __TEXT.__unwind_info: 0x320
-  __TEXT.__eh_frame: 0x390
-  __DATA_CONST.__const: 0x710
+  __TEXT.__unwind_info: 0x3b8
+  __TEXT.__eh_frame: 0x4d0
+  __DATA_CONST.__const: 0x8c8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__auth_got: 0x4c0
-  __DATA_CONST.__got: 0x178
-  __DATA_CONST.__auth_ptr: 0x198
+  __DATA_CONST.__auth_got: 0x4e8
+  __DATA_CONST.__got: 0x1a8
+  __DATA_CONST.__auth_ptr: 0x1b8
   __DATA.__objc_selrefs: 0x40
-  __DATA.__data: 0x218
-  __DATA.__bss: 0x640
-  __DATA.__common: 0x28
+  __DATA.__data: 0x260
+  __DATA.__bss: 0x770
+  __DATA.__common: 0x30
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/Foundation.framework/Versions/C/Foundation
   - /System/Library/Frameworks/IOKit.framework/Versions/A/IOKit

   - /usr/lib/swift/libswiftXPC.dylib
   - /usr/lib/swift/libswift_Builtin_float.dylib
   - /usr/lib/swift/libswift_DarwinFoundation2.dylib
-  Functions: 269
-  Symbols:   257
-  CStrings:  60
+  Functions: 351
+  Symbols:   271
+  CStrings:  58
 
Symbols:
+ _$sSQ2eeoiySbx_xtFZTj
+ _$sSS5index6beforeSS5IndexVAD_tF
+ _$sSS6appendyySJF
+ _$sSSySJSS5IndexVcig
+ _$sSSySSxcSTRzSJ7ElementRtzlufC
+ _$sSs10lowercasedSSyF
+ _$ss10AnyKeyPathCSQsWP
+ _$ss12_ArrayBufferV19_getElementSlowPathyyXlSiFyXl_Ts5
+ _$ss18ReversedCollectionVMn
+ _$ss18ReversedCollectionVyxGSTsMc
+ _$ss18_CocoaArrayWrapperV8endIndexSivg
+ _$ss4Int8VN
+ _$ss5Int64VMn
+ _$ss5Int64VN
+ _$ss5Int64Vs23CustomStringConvertiblesWP
+ _$ss5NeverON
+ _$ss5NeverOs5ErrorsWP
+ _$ss7KeyPathCMn
+ _host_get_special_port
+ _mach_port_deallocate
+ _mach_task_self_
+ _swift_getAtKeyPath
+ _swift_getKeyPath
- _$sSS10lowercasedSSyF
- _$ss15_print_unlockedyyx_q_zts16TextOutputStreamR_r0_lF
- _$ss26DefaultStringInterpolationVN
- _$ss26DefaultStringInterpolationVs16TextOutputStreamsWP
- _mach_error_string
- _swift_bridgeObjectRelease_n
- _swift_deallocClassInstance
- _swift_initStackObject
- _swift_setDeallocating
CStrings:
+ "Expand wired-zone memory into individual zones (requires root)."
+ "Show only the physical-memory summary and swap."
+ "VM_KERN_COUNT_WIRED"
+ "VM_KERN_MEMORY_ZONE"
+ "meminfo: --zones requires root; showing aggregate zone total\n"
- "%10llu pages  %10.1f MB  "
- "Expand wired-zone memory into individual zones."
- "Physical Memory: %llu pages (%.0f MB, page size %llu bytes)"
- "Show static carveout breakdown from device tree."
- "Show wired memory breakdown by kernel site."
- "meminfo: mach_memory_info: error "
- "meminfo: mach_memory_info: permission denied (try running as root)\n"
```
