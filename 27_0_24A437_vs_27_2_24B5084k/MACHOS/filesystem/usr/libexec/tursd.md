## tursd

> `/usr/libexec/tursd`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__const`
- `__TEXT.__swift5_typeref`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_fieldmd`
- `__TEXT.__swift5_builtin`
- `__TEXT.__swift5_assocty`
- `__TEXT.__swift5_proto`
- `__DATA_CONST.__const`
- `__DATA.__objc_const`
- `__DATA.__objc_selrefs`
- `__DATA.__data`

```diff

-1160.0.0.0.0
+1161.1.2.0.0
   __TEXT.__text: 0x8110
   __TEXT.__auth_stubs: 0x5e0
   __TEXT.__objc_stubs: 0x1b40

   __TEXT.__const: 0x1b2
   __TEXT.__cstring: 0xa73
   __TEXT.__oslogstring: 0x2c5
-  __TEXT.__objc_methname: 0x3b0c
+  __TEXT.__objc_methname: 0x3b13
   __TEXT.__objc_classname: 0x146
-  __TEXT.__objc_methtype: 0x92e
+  __TEXT.__objc_methtype: 0x948
   __TEXT.__swift5_typeref: 0x4a
   __TEXT.__constg_swiftt: 0x60
   __TEXT.__swift5_reflstr: 0x1d

   - /usr/lib/swift/libswiftos.dylib
   Functions: 318
   Symbols:   198
-  CStrings:  756
+  CStrings:  757
 
CStrings:
+ "conversationManager:conversation:participant:didUpdateNickname:reason:"
+ "v56@0:8@\"TUConversationManager\"16@\"TUConversation\"24@\"TUConversationParticipant\"32@\"NSString\"40Q48"
+ "v56@0:8@16@24@32@40Q48"
- "conversationManager:conversation:participant:didUpdateNickname:"
- "v48@0:8@\"TUConversationManager\"16@\"TUConversation\"24@\"TUConversationParticipant\"32@\"NSString\"40"
```
