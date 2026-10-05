## nsurlsessiond

> `/usr/libexec/nsurlsessiond`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__got`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-3896.200.41.0.0
-  __TEXT.__text: 0x82618
-  __TEXT.__auth_stubs: 0x11d0
+3896.200.52.0.0
+  __TEXT.__text: 0x82a24
+  __TEXT.__auth_stubs: 0x11e0
   __TEXT.__lazy_helpers: 0xfc
   __TEXT.__objc_stubs: 0xab60
-  __TEXT.__objc_methlist: 0x6334
+  __TEXT.__objc_methlist: 0x633c
   __TEXT.__const: 0x270
-  __TEXT.__gcc_except_tab: 0xe820
+  __TEXT.__gcc_except_tab: 0xe8e4
   __TEXT.__cstring: 0x3cc8
   __TEXT.__objc_methname: 0xf534
   __TEXT.__objc_classname: 0xbd1
   __TEXT.__objc_methtype: 0x2f81
-  __TEXT.__oslogstring: 0xf8cf
-  __TEXT.__unwind_info: 0x3158
+  __TEXT.__oslogstring: 0xf9a2
+  __TEXT.__unwind_info: 0x3160
   __DATA_CONST.__const: 0x15e8
   __DATA_CONST.__cfstring: 0x1e00
   __DATA_CONST.__objc_classlist: 0x240

   __DATA_CONST.__objc_arraydata: 0x18
   __DATA_CONST.__objc_dictobj: 0x28
   __DATA_CONST.__objc_arrayobj: 0x18
-  __DATA_CONST.__auth_got: 0x900
+  __DATA_CONST.__auth_got: 0x908
   __DATA_CONST.__got: 0x7b0
   __DATA_CONST.__auth_ptr: 0x8
   __DATA.__objc_const: 0x9000

   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  Functions: 2102
-  Symbols:   518
-  CStrings:  3899
+  Functions: 2103
+  Symbols:   519
+  CStrings:  3902
 
Symbols:
+ __CFN_isForegroundOnlyAVAssetDownloadIdentifier
CStrings:
+ "%{public}@ cancelling foreground-only AVAssetDownload: client disconnected"
+ "%{public}@ no Live Activity: foreground-only session"
+ "Cleaning up foreground-only session <%{public}@>.<%{public}@>: last task completed"
```
