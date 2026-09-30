## commerce

> `/System/Library/PrivateFrameworks/CommerceKit.framework/Versions/A/Resources/commerce`

### Sections with Same Size but Changed Content

- `__TEXT.__gcc_except_tab`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA_CONST.__got`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_const`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-717.0.7.0.0
-  __TEXT.__text: 0x1e5d40
-  __TEXT.__auth_stubs: 0x680
-  __TEXT.__objc_stubs: 0x41e0
-  __TEXT.__objc_methlist: 0x1214
+717.1.1.0.0
+  __TEXT.__text: 0x1e6588
+  __TEXT.__auth_stubs: 0x690
+  __TEXT.__objc_stubs: 0x4200
+  __TEXT.__objc_methlist: 0x122c
   __TEXT.__const: 0x70210
   __TEXT.__gcc_except_tab: 0x14fc
-  __TEXT.__objc_methname: 0x416c
-  __TEXT.__cstring: 0xcbb
-  __TEXT.__oslogstring: 0x1333
+  __TEXT.__objc_methname: 0x41f2
+  __TEXT.__cstring: 0xcf1
+  __TEXT.__oslogstring: 0x15a9
   __TEXT.__objc_classname: 0x126
   __TEXT.__objc_methtype: 0xfe7
-  __TEXT.__unwind_info: 0xbe0
+  __TEXT.__unwind_info: 0xc08
   __TEXT.__eh_frame: 0xc8
-  __DATA_CONST.__const: 0x1a738
-  __DATA_CONST.__cfstring: 0x1540
+  __DATA_CONST.__const: 0x1a768
+  __DATA_CONST.__cfstring: 0x1580
   __DATA_CONST.__objc_classlist: 0x68
   __DATA_CONST.__objc_protolist: 0x30
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__objc_intobj: 0xa8
   __DATA_CONST.__objc_arraydata: 0x88
   __DATA_CONST.__objc_arrayobj: 0x30
-  __DATA_CONST.__auth_got: 0x350
+  __DATA_CONST.__auth_got: 0x358
   __DATA_CONST.__got: 0x4b8
   __DATA_CONST.__auth_ptr: 0x20
   __DATA.__objc_const: 0x20a0
-  __DATA.__objc_selrefs: 0x1388
+  __DATA.__objc_selrefs: 0x1390
   __DATA.__objc_ivar: 0xc0
   __DATA.__objc_data: 0x410
   __DATA.__data: 0xdf0

   - /System/Library/PrivateFrameworks/SystemAdministration.framework/Versions/A/SystemAdministration
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 736
-  Symbols:   291
-  CStrings:  1155
+  Functions: 748
+  Symbols:   292
+  CStrings:  1165
 
Symbols:
+ _CKURLHostMatchesDomainList
CStrings:
+ "%{public}@ refusing to build a request for untrusted host %{public}@: not matched by any entry in trustedDomains"
+ "%{public}@ refusing to ping untrusted host %{public}@: not matched by any entry in trustedDomains"
+ "%{public}@ refusing to process a store response that is not an NSHTTPURLResponse: %{public}@"
+ "Refusing %{public}@ for host %{public}@: could not load the bag to check trustedDomains: %{public}@"
+ "Refusing %{public}@ for host %{public}@: the bag has no usable trustedDomains list"
+ "Refusing %{public}@ for untrusted host %{public}@: not matched by any entry in trustedDomains"
+ "Refusing to process a store response with no URL"
+ "_pingUrls:trustedDomains:"
+ "processTrustedResponse:forRequest:storeClient:withCompletionHandler:"
+ "to process a store response"
+ "to return a cookie header"
+ "validateTrustedURL:storeClient:reason:withCompletionHandler:"
- "_pingUrls:"
- "hasSuffix:"
```
