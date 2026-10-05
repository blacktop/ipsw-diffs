## tursd

> `/usr/libexec/tursd`

### Sections with Same Size but Changed Content

- `__TEXT.__const`
- `__TEXT.__swift5_typeref`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_fieldmd`
- `__TEXT.__swift5_builtin`
- `__TEXT.__swift5_assocty`
- `__TEXT.__swift5_proto`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__got`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

   __TEXT.__text: 0x8110
   __TEXT.__auth_stubs: 0x5e0
   __TEXT.__objc_stubs: 0x1b40
-  __TEXT.__objc_methlist: 0x1144
+  __TEXT.__objc_methlist: 0x1150
   __TEXT.__const: 0x1b2
   __TEXT.__cstring: 0xa73
   __TEXT.__oslogstring: 0x2c5
-  __TEXT.__objc_methname: 0x3b13
+  __TEXT.__objc_methname: 0x3b4a
   __TEXT.__objc_classname: 0x146
-  __TEXT.__objc_methtype: 0x948
+  __TEXT.__objc_methtype: 0x984
   __TEXT.__swift5_typeref: 0x4a
   __TEXT.__constg_swiftt: 0x60
   __TEXT.__swift5_reflstr: 0x1d

   __DATA_CONST.__auth_got: 0x2f8
   __DATA_CONST.__got: 0x258
   __DATA_CONST.__auth_ptr: 0x58
-  __DATA.__objc_const: 0x17c8
-  __DATA.__objc_selrefs: 0xd00
+  __DATA.__objc_const: 0x17d0
+  __DATA.__objc_selrefs: 0xd08
   __DATA.__objc_ivar: 0x98
   __DATA.__objc_data: 0x2d0
   __DATA.__data: 0x218

   - /usr/lib/swift/libswiftos.dylib
   Functions: 318
   Symbols:   198
-  CStrings:  757
+  CStrings:  759
 
CStrings:
+ "conversationManager:debugSendInterpreterLink:toHandle:"
+ "v40@0:8@\"TUConversationManager\"16@\"NSString\"24@\"NSString\"32"
```
