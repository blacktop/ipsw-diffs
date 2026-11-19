## storagekitd

> `/usr/libexec/storagekitd`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__gcc_except_tab`
- `__TEXT.__info_plist`
- `__TEXT.__unwind_info`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__objc_dictobj`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__got`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-1076.0.4.0.0
-  __TEXT.__text: 0x17b080
-  __TEXT.__auth_stubs: 0x2ee0
+1076.40.4.0.0
+  __TEXT.__text: 0x17d048
+  __TEXT.__auth_stubs: 0x2ec0
   __TEXT.__objc_stubs: 0xeb80
   __TEXT.__objc_methlist: 0x7edc
-  __TEXT.__const: 0xc88
+  __TEXT.__const: 0xc98
   __TEXT.__objc_methname: 0x14cf3
-  __TEXT.__oslogstring: 0x61c6
+  __TEXT.__oslogstring: 0x6263
   __TEXT.__objc_classname: 0xd0d
   __TEXT.__objc_methtype: 0x5da7
-  __TEXT.__cstring: 0x608f2
+  __TEXT.__cstring: 0x60a5d
   __TEXT.__gcc_except_tab: 0x2544
   __TEXT.__info_plist: 0x42d
   __TEXT.__unwind_info: 0x31f8
   __TEXT.__eh_frame: 0x140
   __DATA_CONST.__const: 0x2ab0
-  __DATA_CONST.__cfstring: 0x3af60
+  __DATA_CONST.__cfstring: 0x3b020
   __DATA_CONST.__objc_classlist: 0x418
   __DATA_CONST.__objc_catlist: 0x88
   __DATA_CONST.__objc_protolist: 0xa8

   __DATA_CONST.__objc_arrayobj: 0x8e8
   __DATA_CONST.__objc_dictobj: 0x5c8
   __DATA_CONST.__objc_intobj: 0x168
-  __DATA_CONST.__auth_got: 0x1780
+  __DATA_CONST.__auth_got: 0x1770
   __DATA_CONST.__got: 0xbb0
   __DATA_CONST.__auth_ptr: 0xb0
   __DATA.__objc_const: 0xf1c8

   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libutil.dylib
   Functions: 3579
-  Symbols:   1123
-  CStrings:  13866
+  Symbols:   1121
+  CStrings:  13876
 
Symbols:
- _chmod
- _chown
CStrings:
+ "%s: Not chowning %s: expected %@, got %s (fd=%d errno=%d)"
+ "%s: fchown of %@ failed: errno=%d"
+ "/.nofollow/"
+ "<no fd>"
+ "ASSERT: nil inSessionUUID"
+ "IO entry for %{public}@ does not conform to %{public}@, refusing"
+ "NOT setting owner/mode: fstatfs on volume root failed: mp=%@ errno=%d"
+ "NOT setting owner/mode: mounted disk differs from expected: expected=%@ actual=%s mp=%@"
+ "NOT setting owner/mode: volume root open failed: mp=%@ errno=%d"
+ "bsd=%@ resolved to obj=0x%x of class=%s which does not conform to %s; refusing"
+ "doing setting on verified fd=%d: fchown(UID-->%d GID-->%d); fchmod(MODE-->%o)"
+ "fchmod return=%d errno=%d"
+ "fchown return=%d errno=%d"
- "chmod return=%d errno=%d"
- "chown return=%d errno=%d"
- "doing setting on %s: chmod(MODE-->%o); chown(UID-->%d GID-->%d)"
```
