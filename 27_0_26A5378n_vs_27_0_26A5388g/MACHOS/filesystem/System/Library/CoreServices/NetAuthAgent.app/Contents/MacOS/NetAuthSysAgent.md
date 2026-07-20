## NetAuthSysAgent

> `/System/Library/CoreServices/NetAuthAgent.app/Contents/MacOS/NetAuthSysAgent`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__gcc_except_tab`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__got`
- `__DATA.__objc_const`
- `__DATA.__objc_data`

```diff

-2027.0.2.0.0
-  __TEXT.__text: 0x190d4
+2027.0.3.0.0
+  __TEXT.__text: 0x191cc
   __TEXT.__auth_stubs: 0xd10
-  __TEXT.__objc_stubs: 0x25a0
+  __TEXT.__objc_stubs: 0x25c0
   __TEXT.__objc_methlist: 0x1040
   __TEXT.__const: 0x78
-  __TEXT.__cstring: 0x3975
+  __TEXT.__cstring: 0x3ae5
   __TEXT.__gcc_except_tab: 0x2a0
-  __TEXT.__objc_methname: 0x1f80
+  __TEXT.__objc_methname: 0x1f92
   __TEXT.__objc_classname: 0x15e
   __TEXT.__objc_methtype: 0x425
   __TEXT.__unwind_info: 0x670
   __DATA_CONST.__const: 0x7c0
-  __DATA_CONST.__cfstring: 0x3860
+  __DATA_CONST.__cfstring: 0x3940
   __DATA_CONST.__objc_classlist: 0x50
   __DATA_CONST.__objc_catlist: 0x8
   __DATA_CONST.__objc_imageinfo: 0x8

   __DATA_CONST.__got: 0x2b8
   __DATA_CONST.__auth_ptr: 0x18
   __DATA.__objc_const: 0xbe0
-  __DATA.__objc_selrefs: 0xac0
+  __DATA.__objc_selrefs: 0xac8
   __DATA.__objc_ivar: 0xb8
   __DATA.__objc_data: 0x320
   __DATA.__bss: 0xf0

   - /usr/lib/libobjc.A.dylib
   Functions: 484
   Symbols:   306
-  CStrings:  931
+  CStrings:  939
 
Functions:
~ sub_1000099f0 : 1436 -> 1424
~ sub_10000ac0c -> sub_10000ac00 : 848 -> 824
~ sub_100014118 -> sub_1000140f4 : 868 -> 1152
CStrings:
+ "Agent is not root (no privilege delta over caller) - allowing mount to %@"
+ "Caller has TCC grant for %@ - allowing mount to %@"
+ "Caller is root - allowing mount to %@"
+ "Mount point %@ denied by capability check"
+ "Mount point %@ is TCC-protected (%@); caller lacks the grant - denying"
+ "Mount point %@ is an unprotected location under the caller's home - allowing"
+ "Mount point %@ requires Full Disk Access; caller lacks it - denying"
+ "Movies"
+ "Music"
+ "Pictures"
+ "Root agent asked to mount out-of-home path %@ for a non-root caller without Full Disk Access - denying"
+ "arrayWithObjects:"
- "Caller has Full Disk Access - allowing mount"
- "Caller has TCC grant for %@ - allowing mount"
- "Mount point %@ allowed via TCC grant"
- "Mount point %@ denied - not /Volumes, no TCC grant"
```
