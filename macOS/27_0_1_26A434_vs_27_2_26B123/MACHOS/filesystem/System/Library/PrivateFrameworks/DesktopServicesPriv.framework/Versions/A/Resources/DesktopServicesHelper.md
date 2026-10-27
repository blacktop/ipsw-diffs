## DesktopServicesHelper

> `/System/Library/PrivateFrameworks/DesktopServicesPriv.framework/Versions/A/Resources/DesktopServicesHelper`

### Sections with Same Size but Changed Content

- `__TEXT.__init_offsets`
- `__TEXT.__objc_methlist`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_const`
- `__DATA.__objc_data`

```diff

-1857.0.0.0.0
-  __TEXT.__text: 0x9042c
-  __TEXT.__auth_stubs: 0x1e20
-  __TEXT.__objc_stubs: 0x1bc0
+1857.1.9.100.0
+  __TEXT.__text: 0x924c4
+  __TEXT.__auth_stubs: 0x1e10
+  __TEXT.__objc_stubs: 0x1c00
   __TEXT.__init_offsets: 0x8
   __TEXT.__objc_methlist: 0x604
-  __TEXT.__gcc_except_tab: 0xbe10
-  __TEXT.__const: 0x3410
-  __TEXT.__objc_methname: 0x1900
+  __TEXT.__gcc_except_tab: 0xc1e4
+  __TEXT.__const: 0x3400
+  __TEXT.__objc_methname: 0x191d
   __TEXT.__objc_classname: 0xc7
-  __TEXT.__cstring: 0x30a0
+  __TEXT.__cstring: 0x30f8
   __TEXT.__objc_methtype: 0x89f
-  __TEXT.__oslogstring: 0x3aa5
+  __TEXT.__oslogstring: 0x3c4c
   __TEXT.__ustring: 0x8
-  __TEXT.__info_plist: 0x638
-  __TEXT.__unwind_info: 0x42b0
-  __DATA_CONST.__const: 0x29e0
-  __DATA_CONST.__cfstring: 0x18a0
+  __TEXT.__info_plist: 0x646
+  __TEXT.__unwind_info: 0x4358
+  __DATA_CONST.__const: 0x29d0
+  __DATA_CONST.__cfstring: 0x1860
   __DATA_CONST.__objc_classlist: 0x40
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x10

   __DATA_CONST.__objc_protorefs: 0x10
   __DATA_CONST.__objc_superrefs: 0x30
   __DATA_CONST.__objc_intobj: 0x60
-  __DATA_CONST.__auth_got: 0xf28
-  __DATA_CONST.__got: 0x600
+  __DATA_CONST.__auth_got: 0xf20
+  __DATA_CONST.__got: 0x608
   __DATA_CONST.__auth_ptr: 0x18
   __DATA.__objc_const: 0xa18
-  __DATA.__objc_selrefs: 0x820
+  __DATA.__objc_selrefs: 0x828
   __DATA.__objc_ivar: 0x5c
   __DATA.__objc_data: 0x280
-  __DATA.__data: 0x241
-  __DATA.__bss: 0xe00
+  __DATA.__data: 0x2c9
+  __DATA.__bss: 0xe10
   __DATA.__common: 0x1b8
   - /System/Library/Frameworks/ApplicationServices.framework/Versions/A/ApplicationServices
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation

   - /System/Library/PrivateFrameworks/APFS.framework/Versions/A/APFS
   - /System/Library/PrivateFrameworks/CoreAnalytics.framework/Versions/A/CoreAnalytics
   - /System/Library/PrivateFrameworks/IconServices.framework/Versions/A/IconServices
+  - /System/Library/PrivateFrameworks/TCC.framework/Versions/A/TCC
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libbsm.0.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libfakelink.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 2343
+  Functions: 2367
   Symbols:   690
-  CStrings:  1262
+  CStrings:  1275
 
Symbols:
+ _CFURLIsFileReferenceURL
+ ___cxa_rethrow
+ _kTCCServiceSystemPolicyAllFiles
- __CFURLAttachSecurityScopeToFileURL
- __CFURLCopySecurityScopeFromFileURL
- ___cxa_get_exception_ptr
CStrings:
+ "%{public}s of '%{public}@' failed with %{public}s"
+ "1\"0!0"
+ "1&0!0"
+ "2!0"
+ "Clearing lock flags"
+ "Lookup of '%{public}@' needed FP's cache, but nothing is monitoring the provider list"
+ "Move operation path cache is full, evicting an entry"
+ "NSFileProviderInternalErrorDomain"
+ "Reading path"
+ "Repair"
+ "Repaired owner for '%{public}@', UID changed from %d to %d"
+ "Repaired permissions for '%{public}@' with %lu failure(s), first: '%{public}@'"
+ "Restoring lock flags"
+ "Unarchiving paths"
+ "Unwinding after error - %{public}@"
+ "Validating paths"
+ "_URLByInsertingResolveFlags:"
+ "rename refused a symlinked component on a resolved path\n\t old: `%{public}@`\n\t new: `%{public}@`"
+ "should not invoke DesktopServicesHelper for an AppleScripted operation"
- "%{public}s of '%{public}@' failed with error=%d"
- "1\"0 0"
- "1&0 0"
- "2 0"
- "Repaired owner for '%{public}@, UID changed from %d to %d"
- "kTCCServiceSystemPolicyAllFiles"
```
