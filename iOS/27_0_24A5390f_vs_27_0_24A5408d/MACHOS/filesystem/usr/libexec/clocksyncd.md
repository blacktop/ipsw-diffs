## clocksyncd

> `/usr/libexec/clocksyncd`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__gcc_except_tab`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__got`
- `__DATA.__objc_const`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-1501.5.0.0.0
-  __TEXT.__text: 0x3b028
+1501.6.0.0.0
+  __TEXT.__text: 0x3b364
   __TEXT.__auth_stubs: 0xd30
-  __TEXT.__objc_stubs: 0x59e0
+  __TEXT.__objc_stubs: 0x5a00
   __TEXT.__objc_methlist: 0x36b4
   __TEXT.__const: 0x129
-  __TEXT.__cstring: 0x27e0
-  __TEXT.__oslogstring: 0x5853
+  __TEXT.__cstring: 0x2835
+  __TEXT.__oslogstring: 0x592c
   __TEXT.__gcc_except_tab: 0x1aa8
-  __TEXT.__objc_methname: 0x9192
+  __TEXT.__objc_methname: 0x919d
   __TEXT.__objc_classname: 0x508
   __TEXT.__objc_methtype: 0x197a
-  __TEXT.__unwind_info: 0xe78
+  __TEXT.__unwind_info: 0xe80
   __DATA_CONST.__const: 0x948
-  __DATA_CONST.__cfstring: 0x1ee0
+  __DATA_CONST.__cfstring: 0x1f00
   __DATA_CONST.__objc_classlist: 0x168
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_protolist: 0x78

   __DATA_CONST.__got: 0x278
   __DATA_CONST.__auth_ptr: 0x110
   __DATA.__objc_const: 0x6a28
-  __DATA.__objc_selrefs: 0x1d98
+  __DATA.__objc_selrefs: 0x1da0
   __DATA.__objc_ivar: 0x514
   __DATA.__objc_data: 0xe10
   __DATA.__data: 0x5a8

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 1528
+  Functions: 1532
   Symbols:   281
-  CStrings:  2453
+  CStrings:  2459
 
CStrings:
+ "1501.6"
+ "IOTimeSync"
+ "_isAllowedRegistryRead(service, key)"
+ "_isAllowedRegistryRead(service, nil)"
+ "hasPrefix:"
+ "propertiesForRegistryEntryID rejected: entryID=0x%llx class=%{public}@ (not in TimeSync object graph)"
+ "propertyForRegistryEntryID rejected: entryID=0x%llx key=%{public}@ class=%{public}@ (not in TimeSync object graph)"
- "1501.5"
```
