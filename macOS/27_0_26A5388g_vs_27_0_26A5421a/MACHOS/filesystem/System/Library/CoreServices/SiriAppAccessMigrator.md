## SiriAppAccessMigrator

> `/System/Library/CoreServices/SiriAppAccessMigrator`

### Sections with Same Size but Changed Content

- `__TEXT.__unwind_info`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_arrayobj`
- `__DATA.__objc_selrefs`

```diff

-3600.68.44.0.0
-  __TEXT.__text: 0xd20
+3600.68.61.14.4
+  __TEXT.__text: 0xd1c
   __TEXT.__auth_stubs: 0x1c0
   __TEXT.__objc_stubs: 0x120
   __TEXT.__const: 0x38
-  __TEXT.__oslogstring: 0x4c2
-  __TEXT.__cstring: 0x11f
+  __TEXT.__oslogstring: 0x4ce
+  __TEXT.__cstring: 0x135
   __TEXT.__objc_methname: 0x8e
   __TEXT.__unwind_info: 0x68
   __DATA_CONST.__const: 0x60
-  __DATA_CONST.__cfstring: 0x1a0
+  __DATA_CONST.__cfstring: 0x1c0
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_arraydata: 0x28
   __DATA_CONST.__objc_arrayobj: 0x18
   __DATA_CONST.__auth_got: 0xe8
-  __DATA_CONST.__got: 0x48
+  __DATA_CONST.__got: 0x40
   __DATA.__objc_selrefs: 0x48
   __DATA.__bss: 0x20
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   Functions: 5
-  Symbols:   43
-  CStrings:  42
+  Symbols:   42
+  CStrings:  43
 
Symbols:
- _kTCCServiceSiri
Functions:
~ sub_1000009c8 : 2408 -> 2404
CStrings:
+ "First TCC write failure — to triage, run on the device: codesign -dv --entitlements - /System/Library/CoreServices/SiriAppAccessMigrator. Expect com.apple.private.tcc.manager.access.modify -> kTCCServiceSiriAccess."
+ "Marked %{public}@ as denied in kTCCServiceSiriAccess. [sources: LFTA=%{public}@, ShowContent=%{public}@]"
+ "kTCCServiceSiriAccess"
- "First TCC write failure — to triage, run on the device: codesign -dv --entitlements - /System/Library/CoreServices/SiriAppAccessMigrator. Expect com.apple.private.tcc.manager.access.modify -> kTCCServiceSiri."
- "Marked %{public}@ as denied in kTCCServiceSiri. [sources: LFTA=%{public}@, ShowContent=%{public}@]"
```
