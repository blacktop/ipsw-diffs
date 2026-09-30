## eligibilityd

> `/usr/libexec/eligibilityd`

```diff

-181.100.8.502.6
-  __TEXT.__text: 0x26078
-  __TEXT.__auth_stubs: 0x12a0
-  __TEXT.__objc_stubs: 0x1c20
-  __TEXT.__objc_methlist: 0x1354
-  __TEXT.__const: 0xd88
-  __TEXT.__objc_methname: 0x1d03
+181.100.26.0.0
+  __TEXT.__text: 0x26988
+  __TEXT.__auth_stubs: 0x1340
+  __TEXT.__objc_stubs: 0x1c40
+  __TEXT.__objc_methlist: 0x135c
+  __TEXT.__const: 0xd80
+  __TEXT.__objc_methname: 0x1d21
   __TEXT.__swift5_typeref: 0x462
-  __TEXT.__oslogstring: 0x1b58
-  __TEXT.__cstring: 0x4266
+  __TEXT.__oslogstring: 0x1d6d
+  __TEXT.__cstring: 0x43c1
   __TEXT.__constg_swiftt: 0x464
-  __TEXT.__swift5_reflstr: 0x2b7
+  __TEXT.__swift5_reflstr: 0x2b3
   __TEXT.__swift5_fieldmd: 0x410
   __TEXT.__swift5_builtin: 0x50
   __TEXT.__swift5_assocty: 0x48

   __TEXT.__gcc_except_tab: 0x298
   __TEXT.__objc_classname: 0x236
   __TEXT.__objc_methtype: 0x2be
-  __TEXT.__unwind_info: 0x878
+  __TEXT.__unwind_info: 0x888
   __TEXT.__eh_frame: 0x6d8
-  __DATA_CONST.__auth_got: 0x960
+  __DATA_CONST.__auth_got: 0x9b0
   __DATA_CONST.__got: 0x2b0
-  __DATA_CONST.__auth_ptr: 0x2a8
-  __DATA_CONST.__const: 0x18d8
-  __DATA_CONST.__cfstring: 0x3180
+  __DATA_CONST.__auth_ptr: 0x2a0
+  __DATA_CONST.__const: 0x1910
+  __DATA_CONST.__cfstring: 0x3340
   __DATA_CONST.__objc_classlist: 0xc8
   __DATA_CONST.__objc_protolist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0xb0
   __DATA_CONST.__objc_intobj: 0x1b0
-  __DATA_CONST.__objc_arraydata: 0x4210
-  __DATA_CONST.__objc_arrayobj: 0xe10
-  __DATA_CONST.__objc_dictobj: 0x3e58
+  __DATA_CONST.__objc_arraydata: 0x4428
+  __DATA_CONST.__objc_arrayobj: 0xe88
+  __DATA_CONST.__objc_dictobj: 0x3fc0
   __DATA.__objc_const: 0x21a0
-  __DATA.__objc_selrefs: 0x868
+  __DATA.__objc_selrefs: 0x870
   __DATA.__objc_ivar: 0x8c
   __DATA.__objc_data: 0x810
   __DATA.__data: 0x770

   - /usr/lib/swift/libswiftsimd.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  Functions: 748
-  Symbols:   485
-  CStrings:  1327
+  Functions: 751
+  Symbols:   495
+  CStrings:  1360
 
Symbols:
+ _close
+ _fstat
+ _mmap
+ _munmap
+ _objc_retainBlock
+ _open
+ _os_eligibility_domain_for_name
+ _swift_cvw_assignWithCopy
+ _swift_cvw_assignWithTake
+ _swift_cvw_destroy
+ _swift_cvw_enumFn_getEnumTag
+ _swift_cvw_initWithCopy
+ _swift_cvw_initializeBufferWithCopyOfBuffer
+ _xpc_create_from_plist
+ _xpc_dictionary_apply
+ _xpc_release
- _swift_enumFn_getEnumTag
- _swift_generic_assignWithCopy
- _swift_generic_assignWithTake
- _swift_generic_destroy
- _swift_generic_initWithCopy
- _swift_generic_initializeBufferWithCopyOfBuffer
CStrings:
+ "%s: Answer plist %llu unexpectedly returned a non-dictionary object"
+ "%s: Expected plist to be a dictionary but instead was a %s"
+ "%s: Failed to map file at %s; error: %s"
+ "%s: Failed to open %s: %s(%d)"
+ "%s: Failed to parse property list"
+ "%s: Failed to stat %s: %s(%d)"
+ "%s: Unable to load the current eligibility answers on disk, skipping file %llu: %d"
+ "%s: Unknown domain %s read from file %llu"
+ "%s: Unknown eligibility answer file type: %llu"
+ "%s: Unsupported domain %llu; falling back to private plist"
+ "%s: eligibility plist is too large (%zu)"
+ "-[EligibilityEngine _loadCurrentEligibilityOnDisk]"
+ "-[EligibilityEngine _loadCurrentEligibilityOnDisk]_block_invoke"
+ "03:19:02"
+ "129"
+ "181.100.26"
+ "AR"
+ "B24@?0r*8@\"NSObject<OS_xpc_object>\"16"
+ "CL"
+ "CO"
+ "DO"
+ "Feb 22 2025"
+ "HK"
+ "IL"
+ "KZ"
+ "MX"
+ "MY"
+ "OS_ELIGIBILITY_DOMAIN_HIGHLIGHTS_MARKETPLACES"
+ "PE"
+ "SG"
+ "TW"
+ "_loadCurrentEligibilityOnDisk"
+ "copy_eligibility_file_path"
+ "eligibility_domain_to_file"
+ "iOSIneligibleInEUFallbackToLocation"
+ "load_eligibility_plist"
- "07:44:52"
- "181.100.8.502.6"
- "Feb 16 2025"

```
