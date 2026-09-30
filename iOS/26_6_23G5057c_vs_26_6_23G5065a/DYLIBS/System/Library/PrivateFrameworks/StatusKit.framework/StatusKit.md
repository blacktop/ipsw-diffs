## StatusKit

> `/System/Library/PrivateFrameworks/StatusKit.framework/StatusKit`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__const`
- `__TEXT.__swift5_typeref`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_proto`
- `__TEXT.__unwind_info`
- `__DATA_CONST.__got`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_catlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_selrefs`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_arraydata`
- `__AUTH_CONST.__const`
- `__AUTH_CONST.__objc_const`
- `__AUTH_CONST.__objc_dictobj`
- `__AUTH_CONST.__objc_arrayobj`
- `__AUTH.__objc_data`
- `__AUTH.__data`
- `__DATA.__data`
- `__DATA_DIRTY.__objc_data`

```diff

-  __TEXT.__text: 0x20eac
+  __TEXT.__text: 0x20da0
   __TEXT.__auth_stubs: 0x640
   __TEXT.__objc_methlist: 0x1ff8
   __TEXT.__const: 0x192
-  __TEXT.__gcc_except_tab: 0xed0
+  __TEXT.__gcc_except_tab: 0xeb8
   __TEXT.__oslogstring: 0x4b84
-  __TEXT.__cstring: 0x1864
+  __TEXT.__cstring: 0x17c4
   __TEXT.__swift5_typeref: 0x30
   __TEXT.__constg_swiftt: 0x7c
   __TEXT.__swift5_reflstr: 0x22

   __DATA_CONST.__objc_arraydata: 0xc0
   __AUTH_CONST.__auth_got: 0x330
   __AUTH_CONST.__const: 0x340
-  __AUTH_CONST.__cfstring: 0x1080
+  __AUTH_CONST.__cfstring: 0x1040
   __AUTH_CONST.__objc_const: 0x3168
   __AUTH_CONST.__objc_dictobj: 0x28
   __AUTH_CONST.__objc_arrayobj: 0x18

   - /usr/lib/swift/libswiftos.dylib
   Functions: 900
   Symbols:   1779
-  CStrings:  1267
+  CStrings:  1265
 
Functions:
~ -[SKPresence assertPresenceOnChannel:withPresencePayload:persistentPayload:serverRoutablePayload:assertionOptions:completion:] : 1052 -> 920
~ -[SKPresence retainTransientSubscriptionAssertionOnChannel:completion:] : 1076 -> 940
CStrings:
- "Attempted to assert on channel that is not equivalent to active channel"
- "Attempted to retain subscription on channel that is not equivalent to active channel"
```
