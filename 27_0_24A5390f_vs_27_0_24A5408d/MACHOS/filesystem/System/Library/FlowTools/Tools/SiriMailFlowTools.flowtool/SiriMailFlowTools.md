## SiriMailFlowTools

> `/System/Library/FlowTools/Tools/SiriMailFlowTools.flowtool/SiriMailFlowTools`

### Sections with Same Size but Changed Content

- `__TEXT.__constg_swiftt`
- `__TEXT.__swift5_fieldmd`
- `__TEXT.__swift5_assocty`
- `__TEXT.__swift5_proto`
- `__TEXT.__swift5_types`
- `__TEXT.__swift_as_entry`
- `__TEXT.__swift5_capture`
- `__TEXT.__swift5_protos`
- `__DATA_CONST.__const`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__auth_ptr`

```diff

-3600.23.14.0.0
-  __TEXT.__text: 0x49f58
-  __TEXT.__auth_stubs: 0x1480
-  __TEXT.__objc_stubs: 0x460
-  __TEXT.__const: 0x16c0
+3600.23.24.0.0
+  __TEXT.__text: 0x4b4e0
+  __TEXT.__auth_stubs: 0x1500
+  __TEXT.__objc_stubs: 0x500
+  __TEXT.__objc_methlist: 0x154
+  __TEXT.__const: 0x16d0
   __TEXT.__constg_swiftt: 0x3d4
-  __TEXT.__swift5_typeref: 0x6b8
+  __TEXT.__swift5_typeref: 0x6e2
   __TEXT.__swift5_reflstr: 0x5c9
   __TEXT.__swift5_fieldmd: 0x608
   __TEXT.__swift5_assocty: 0x78
   __TEXT.__cstring: 0x2a4
-  __TEXT.__oslogstring: 0x13da
+  __TEXT.__oslogstring: 0x14aa
   __TEXT.__swift5_proto: 0xb0
   __TEXT.__swift5_types: 0x3c
+  __TEXT.__objc_classname: 0x12d
+  __TEXT.__objc_methname: 0x62a
+  __TEXT.__objc_methtype: 0x101
   __TEXT.__swift_as_entry: 0xe4
-  __TEXT.__swift_as_ret: 0x218
-  __TEXT.__swift_as_cont: 0x3c8
+  __TEXT.__swift_as_ret: 0x21c
+  __TEXT.__swift_as_cont: 0x3d0
   __TEXT.__swift5_capture: 0xf0
-  __TEXT.__objc_classname: 0xed
-  __TEXT.__objc_methname: 0x411
-  __TEXT.__objc_methtype: 0x1
   __TEXT.__swift5_protos: 0x14
-  __TEXT.__unwind_info: 0x1420
-  __TEXT.__eh_frame: 0x3d98
+  __TEXT.__unwind_info: 0x1450
+  __TEXT.__eh_frame: 0x3e00
   __DATA_CONST.__const: 0xba8
   __DATA_CONST.__objc_classlist: 0x28
+  __DATA_CONST.__objc_protolist: 0x50
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__auth_got: 0xa48
-  __DATA_CONST.__got: 0x378
+  __DATA_CONST.__objc_protorefs: 0x28
+  __DATA_CONST.__auth_got: 0xa88
+  __DATA_CONST.__got: 0x3a0
   __DATA_CONST.__auth_ptr: 0x780
-  __DATA.__objc_const: 0xad8
-  __DATA.__objc_selrefs: 0x118
-  __DATA.__data: 0xa90
+  __DATA.__objc_const: 0xc38
+  __DATA.__objc_selrefs: 0x200
+  __DATA.__data: 0xc88
   __DATA.__bss: 0x1520
   - /System/Library/Frameworks/AppIntents.framework/AppIntents
+  - /System/Library/Frameworks/Contacts.framework/Contacts
   - /System/Library/Frameworks/Foundation.framework/Foundation
   - /System/Library/Frameworks/Speech.framework/Speech
   - /System/Library/Frameworks/UIKit.framework/UIKit

   - /usr/lib/swift/libswift_Concurrency.dylib
   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsimd.dylib
-  Functions: 1557
-  Symbols:   157
-  CStrings:  132
+  Functions: 1575
+  Symbols:   165
+  CStrings:  192
 
Symbols:
+ _CNContactIdentifierKey
+ _OBJC_CLASS_$_CNContact
+ _OBJC_CLASS_$_CNContactFormatter
+ _OBJC_CLASS_$_CNContactStore
+ ___stack_chk_fail
+ ___stack_chk_guard
+ _objc_retain_x20
+ _objc_retain_x25
CStrings:
+ "#16@0:8"
+ "#MailFlowTool foregrounded app %s differs from executing app %s, but composing/sending with attachments in display mode — letting AppIntent execute in foreground so the user can see the attachment in the full UI"
+ "#SendDraftMailTool registering draft snippet for send confirmation (foregroundApp=%s, sendingApp=%s)"
+ "#UpdateDraftMailTool Parameter `target` not found for tool definition %s"
+ "@\"NSString\"16@0:8"
+ "@16@0:8"
+ "@24@0:8:16"
+ "@24@0:8@\"NSCoder\"16"
+ "@24@0:8@16"
+ "@24@0:8^{_NSZone=}16"
+ "@32@0:8:16@24"
+ "@40@0:8:16@24@32"
+ "B16@0:8"
+ "B24@0:8#16"
+ "B24@0:8:16"
+ "B24@0:8@\"Protocol\"16"
+ "B24@0:8@16"
+ "CNKeyDescriptor"
+ "NSCoding"
+ "NSCopying"
+ "NSObject"
+ "NSSecureCoding"
+ "Q16@0:8"
+ "T#,R"
+ "T@\"NSString\",?,R,C"
+ "T@\"NSString\",R,C"
+ "TB,R"
+ "TQ,R"
+ "Vv16@0:8"
+ "^{_NSZone=}16@0:8"
+ "autorelease"
+ "class"
+ "conformsToProtocol:"
+ "copyWithZone:"
+ "debugDescription"
+ "description"
+ "descriptorForRequiredKeysForStyle:"
+ "encodeWithCoder:"
+ "hash"
+ "identifier"
+ "initWithCoder:"
+ "isEqual:"
+ "isKindOfClass:"
+ "isMemberOfClass:"
+ "isProxy"
+ "performSelector:"
+ "performSelector:withObject:"
+ "performSelector:withObject:withObject:"
+ "predicateForContactsMatchingEmailAddress:"
+ "release"
+ "respondsToSelector:"
+ "retain"
+ "retainCount"
+ "self"
+ "stringFromContact:style:"
+ "superclass"
+ "supportsSecureCoding"
+ "unifiedContactsMatchingPredicate:keysToFetch:error:"
+ "v24@0:8@\"NSCoder\"16"
+ "v24@0:8@16"
+ "zone"
- "#MailFlowTool foregrounded app %s differs from executing app %s, but composing with attachments in display mode — letting AppIntent execute in foreground so the user can see the attachment in the full UI"
```
