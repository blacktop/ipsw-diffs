## smbclientd

> `/System/Library/PrivateFrameworks/SMBClientProvider.framework/smbclientd`

```diff

-231.120.1.0.1
-  __TEXT.__text: 0x5dfd4
-  __TEXT.__auth_stubs: 0x7b0
-  __TEXT.__objc_stubs: 0x5340
-  __TEXT.__objc_methlist: 0x2138
+245.0.0.0.1
+  __TEXT.__text: 0x59b84
+  __TEXT.__auth_stubs: 0x850
+  __TEXT.__objc_stubs: 0x5400
+  __TEXT.__objc_methlist: 0x2170
   __TEXT.__const: 0x2cc
-  __TEXT.__cstring: 0x143c
-  __TEXT.__oslogstring: 0xe26d
-  __TEXT.__objc_classname: 0x1ca
-  __TEXT.__objc_methname: 0x65fa
-  __TEXT.__objc_methtype: 0x2011
-  __TEXT.__gcc_except_tab: 0x29fc
+  __TEXT.__cstring: 0x14c8
+  __TEXT.__oslogstring: 0xe2dd
+  __TEXT.__objc_classname: 0x1a7
+  __TEXT.__objc_methname: 0x6668
+  __TEXT.__objc_methtype: 0x202a
+  __TEXT.__gcc_except_tab: 0x218c
   __TEXT.__ustring: 0x4
-  __TEXT.__unwind_info: 0x1380
-  __DATA_CONST.__auth_got: 0x3e8
-  __DATA_CONST.__got: 0x2e0
-  __DATA_CONST.__const: 0x22e8
+  __TEXT.__unwind_info: 0x13c0
+  __DATA_CONST.__const: 0x2270
   __DATA_CONST.__cfstring: 0xb20
   __DATA_CONST.__objc_classlist: 0xa0
   __DATA_CONST.__objc_protolist: 0x30

   __DATA_CONST.__objc_intobj: 0x30
   __DATA_CONST.__objc_arraydata: 0x10
   __DATA_CONST.__objc_arrayobj: 0x18
+  __DATA_CONST.__auth_got: 0x438
+  __DATA_CONST.__got: 0x2e0
   __DATA.__objc_const: 0x2f40
-  __DATA.__objc_selrefs: 0x1a08
+  __DATA.__objc_selrefs: 0x1a30
   __DATA.__objc_ivar: 0x2c8
   __DATA.__objc_data: 0x640
   __DATA.__data: 0x294

   - /System/Library/PrivateFrameworks/SMBSearch.framework/SMBSearch
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: CCBF4381-74CE-3917-A6A6-D99D5B389D8E
-  Functions: 2284
-  Symbols:   230
-  CStrings:  2657
+  UUID: FA918F18-A664-3A6E-AE9C-693F0C216725
+  Functions: 2281
+  Symbols:   240
+  CStrings:  2666
 
Symbols:
+ _SMBGetFileSystemRepresentation
+ _objc_claimAutoreleasedReturnValue
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x1
+ _objc_retain_x10
+ _objc_retain_x2
+ _objc_retain_x3
+ _objc_retain_x5
+ _objc_retain_x6
+ _objc_retain_x7
+ _objc_retain_x9
- _objc_retainAutoreleasedReturnValue
CStrings:
+ "%s: unable to normalize name: %@, err: %d"
+ "-[smbMount nameTableFindNode:LookupName:]"
+ "-[smbMount nameTableInsertNode:]"
+ "-[smbMount nameTableRemoveNode:]"
+ "LiAccessCheck: np: %@, access: 0x%x, access denied for read-only node"
+ "isImmutable"
+ "nameTableFindNode:LookupName:"
+ "nameTableInsertNode:"
+ "nameTableRemoveNode:"
+ "nodeIsSubDir:OfParentDir:"
+ "v60@0:8@16I24@28@36^{smb_create=QCIIIIII^vIICCIQQQQQQII{?=QQ}QQ{smb_resolve_id=QI}{smb2_lease=QIIQQQQSSiqI}{smb2_durable_handle=Q{?=QQ}II[16C]}}44@?52"
- "v60@0:8@16I24@28@36^{smb_create=QCIIIIII^vIICCIQQQQQQII{?=QQ}{smb_resolve_id=QI}{smb_dur_handle=QQIQQSI[16C]{?=QQ}QII}}44@?52"

```
