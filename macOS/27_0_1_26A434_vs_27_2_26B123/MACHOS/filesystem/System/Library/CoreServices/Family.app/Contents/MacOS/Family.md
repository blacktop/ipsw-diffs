## Family

> `/System/Library/CoreServices/Family.app/Contents/MacOS/Family`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_methlist`
- `__TEXT.__const`
- `__TEXT.__objc_methname`
- `__TEXT.__swift5_typeref`
- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift_as_ret`
- `__TEXT.__swift_as_cont`
- `__TEXT.__unwind_info`
- `__TEXT.__eh_frame`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__got`
- `__DATA_CONST.__auth_ptr`
- `__DATA.__objc_const`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-290.3.1.0.0
-  __TEXT.__text: 0x8f1c
-  __TEXT.__auth_stubs: 0x7d0
-  __TEXT.__objc_stubs: 0x6e0
+291.125.8.0.0
+  __TEXT.__text: 0x90d4
+  __TEXT.__auth_stubs: 0x7c0
+  __TEXT.__objc_stubs: 0x6c0
   __TEXT.__objc_methlist: 0x668
   __TEXT.__const: 0x234
   __TEXT.__gcc_except_tab: 0x10
-  __TEXT.__cstring: 0x190
-  __TEXT.__oslogstring: 0x588
+  __TEXT.__cstring: 0x1b0
+  __TEXT.__oslogstring: 0x5e8
   __TEXT.__objc_classname: 0x215
   __TEXT.__objc_methname: 0xec6
   __TEXT.__objc_methtype: 0x5e5

   __DATA_CONST.__objc_protolist: 0x40
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x28
-  __DATA_CONST.__auth_got: 0x3f8
+  __DATA_CONST.__auth_got: 0x3f0
   __DATA_CONST.__got: 0x118
   __DATA_CONST.__auth_ptr: 0x98
   __DATA.__objc_const: 0xa68
-  __DATA.__objc_selrefs: 0x438
+  __DATA.__objc_selrefs: 0x430
   __DATA.__objc_ivar: 0x14
   __DATA.__objc_data: 0x250
   __DATA.__data: 0x2b0

   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
   Functions: 209
-  Symbols:   217
-  CStrings:  267
+  Symbols:   216
+  CStrings:  268
 
Symbols:
+ _FAUniversalLinkActionShowFamilySettings
- _$ss12_ArrayBufferV19_getElementSlowPathyyXlSiFyXl_Ts5
- _FAUniversalLinkActionAddMember
Functions:
~ sub_100004498 : 1644 -> 1996
~ sub_100004b04 -> sub_100004c64 : 1512 -> 1856
~ sub_1000051d0 -> sub_100005488 : 1048 -> 792
CStrings:
+ "handleFamilyInvite: Universal Web Link inviteCode is organizer_create"
+ "handleFamilyInvite: no pending invite in cached payload, presenting directly"
+ "handleFamilyInvite: pending invite in cached payload, routing through System Settings"
+ "hasPendingInvite: cache fetch failed, treating as no pending invite: %s"
+ "organizer_create"
- "code"
- "handleFamilyInvite: invite not in cached payload, presenting directly"
- "handleFamilyInvite: server-tracked invite, routing through System Settings"
- "isInviteServerTracked: cache fetch failed, treating as untracked: %s"
```
