## MCXCompositor

> `/System/Library/CoreServices/ManagedClient.app/Contents/Resources/MCXCompositor`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_const`
- `__DATA.__objc_data`

```diff

-1841.0.0.0.0
-  __TEXT.__text: 0xd380
-  __TEXT.__auth_stubs: 0xa20
-  __TEXT.__objc_stubs: 0x980
+1842.1.1.0.0
+  __TEXT.__text: 0xd80c
+  __TEXT.__auth_stubs: 0xa40
+  __TEXT.__objc_stubs: 0x9c0
   __TEXT.__objc_methlist: 0x1ec
   __TEXT.__const: 0xe0
-  __TEXT.__gcc_except_tab: 0x6e4
+  __TEXT.__gcc_except_tab: 0x71c
   __TEXT.__objc_classname: 0x23
-  __TEXT.__objc_methname: 0x991
+  __TEXT.__objc_methname: 0x9ae
   __TEXT.__objc_methtype: 0xd7
-  __TEXT.__cstring: 0x4130
-  __TEXT.__oslogstring: 0x1fc2
-  __TEXT.__unwind_info: 0x398
+  __TEXT.__cstring: 0x43ab
+  __TEXT.__oslogstring: 0x2067
+  __TEXT.__unwind_info: 0x3b0
   __DATA_CONST.__const: 0x90
-  __DATA_CONST.__cfstring: 0x8a0
+  __DATA_CONST.__cfstring: 0x8e0
   __DATA_CONST.__objc_classlist: 0x8
   __DATA_CONST.__objc_catlist: 0x28
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_superrefs: 0x8
-  __DATA_CONST.__auth_got: 0x528
-  __DATA_CONST.__got: 0x110
+  __DATA_CONST.__auth_got: 0x538
+  __DATA_CONST.__got: 0x118
   __DATA_CONST.__auth_ptr: 0x8
   __DATA.__objc_const: 0x240
-  __DATA.__objc_selrefs: 0x328
+  __DATA.__objc_selrefs: 0x338
   __DATA.__objc_ivar: 0x8
   __DATA.__objc_data: 0x50
   __DATA.__data: 0x8

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 178
-  Symbols:   208
-  CStrings:  464
+  Functions: 180
+  Symbols:   211
+  CStrings:  474
 
Symbols:
+ _CFStringGetLength
+ _OBJC_CLASS_$_NSMutableData
+ _read
CStrings:
+ "%@/%@"
+ "%@/%@.plist"
+ "---_CFPreferencesWriteManagedDomainForUser_Internal: elided unchanged domainID = %s"
+ "MCX_CopyOnDiskManagedDomain: unable to allocate %lld bytes for %s; will not elide"
+ "TBundlePrefsList::CompositeBundles: composite unchanged but %ld removed-bundle notifications required; posting"
+ "TBundlePrefsList::CompositeBundles: composited output identical to on-disk complete.plist; will elide complete.plist rewrite and aggregate notification"
+ "TBundlePrefsList::CompositeBundles: elided complete.plist rewrite (unchanged)"
+ "TBundlePrefsList::CompositeBundles: no bundle notifications required; skipping MCXPrefsWereUpdatedNotification"
+ "_CFPreferencesWriteManagedDomainForUser_Internal: unable to access output path = %s"
+ "dataWithLength:"
+ "mutableBytes"
- "_CFPreferencesWriteManagedDomainForUser_Internal: unable to access output path = %s."
```
