## MailQuickLookExtension

> `/System/Applications/Mail.app/Contents/PlugIns/MailQuickLookExtension.appex/Contents/MacOS/MailQuickLookExtension`

### Sections with Same Size but Changed Content

- `__TEXT.__objc_classname`
- `__TEXT.__gcc_except_tab`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_dictobj`
- `__DATA.__objc_const`
- `__DATA.__objc_ivar`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-3901.100.1.1.12
-  __TEXT.__text: 0xad50
-  __TEXT.__auth_stubs: 0x3b0
-  __TEXT.__objc_stubs: 0x31c0
-  __TEXT.__objc_methlist: 0xe0c
-  __TEXT.__const: 0x54
-  __TEXT.__cstring: 0x909
-  __TEXT.__objc_methname: 0x3e0b
-  __TEXT.__oslogstring: 0x466
+3901.200.71.1.16
+  __TEXT.__text: 0xb340
+  __TEXT.__auth_stubs: 0x3c0
+  __TEXT.__objc_stubs: 0x33c0
+  __TEXT.__objc_methlist: 0xe7c
+  __TEXT.__objc_methname: 0x4028
   __TEXT.__objc_classname: 0x192
-  __TEXT.__objc_methtype: 0x13ee
+  __TEXT.__cstring: 0x918
+  __TEXT.__objc_methtype: 0x1459
+  __TEXT.__const: 0x5c
   __TEXT.__gcc_except_tab: 0x90
-  __TEXT.__unwind_info: 0x3f8
-  __DATA_CONST.__const: 0x420
+  __TEXT.__oslogstring: 0x537
+  __TEXT.__unwind_info: 0x428
+  __DATA_CONST.__const: 0x440
   __DATA_CONST.__cfstring: 0x780
   __DATA_CONST.__objc_classlist: 0x58
   __DATA_CONST.__objc_protolist: 0x58

   __DATA_CONST.__objc_floatobj: 0x10
   __DATA_CONST.__objc_arraydata: 0x10
   __DATA_CONST.__objc_dictobj: 0x28
-  __DATA_CONST.__auth_got: 0x1e8
-  __DATA_CONST.__got: 0x348
+  __DATA_CONST.__auth_got: 0x1f0
+  __DATA_CONST.__got: 0x360
   __DATA.__objc_const: 0x1cc8
-  __DATA.__objc_selrefs: 0x1170
+  __DATA.__objc_selrefs: 0x11e8
   __DATA.__objc_ivar: 0xa4
   __DATA.__objc_data: 0x370
   __DATA.__data: 0x430
-  __DATA.__bss: 0x50
+  __DATA.__bss: 0x60
   - /System/Library/Frameworks/AppKit.framework/Versions/C/AppKit
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/Versions/A/CoreServices

   - /System/Library/PrivateFrameworks/Synapse.framework/Versions/A/Synapse
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 258
-  Symbols:   223
-  CStrings:  903
+  Functions: 269
+  Symbols:   227
+  CStrings:  922
 
Symbols:
+ _MCLogSubsystem
+ _NSEventTrackingRunLoopMode
+ _OBJC_CLASS_$_NSDate
+ _OBJC_CLASS_$_NSEvent
+ _OBJC_CLASS_$_NSTokenAttachmentCell
- _OBJC_CLASS_$_NSApplication
CStrings:
+ "@\"<MessageWebDocumentViewRedundantContentDelegate>\""
+ "Showing token menu with %ld items for touch tap"
+ "T@\"<MessageWebDocumentViewRedundantContentDelegate>\",W,N,V_redundantContentDelegate"
+ "Token reported a menu but it was empty for touch tap; falling back to token tracking"
+ "Touch on token is not a tap (no queued mouse up); passing to token tracking"
+ "_hasMenuForTokenAttachmentCell:"
+ "_hasUpcomingSyntheticMouseUp"
+ "_lastInteractionWasDirectTouch"
+ "_menuForTokenAttachmentCell:"
+ "_redundantContentDelegate"
+ "_selectTokenAtCharacterIndex:"
+ "_showMenu:forTokenAttachmentCell:atCharacterIndex:inRect:atLocation:"
+ "_tokenAttachmentForCell:"
+ "clickCount"
+ "dateWithTimeIntervalSinceNow:"
+ "delegate"
+ "hasMenuForTokenAttachment:"
+ "menuForTokenAttachment:"
+ "messageWebDocumentView:didRequestRedundantContentExpansionAtIndex:"
+ "nextEventMatchingMask:untilDate:inMode:dequeue:"
+ "numberOfItems"
+ "popUpMenuPositioningItem:atLocation:inView:"
+ "redundantContentDelegate"
+ "selectedRange"
+ "setRedundantContentDelegate:"
+ "type"
+ "v24@0:8Q16"
+ "v88@0:8@16@24Q32{CGRect={CGPoint=dd}{CGSize=dd}}40{CGPoint=dd}72"
- "Tq,N,V_currentClusterIndex"
- "_currentClusterIndex"
- "currentClusterIndex"
- "performRedundantTextExpansion:"
- "q16@0:8"
- "sendAction:to:from:"
- "setCurrentClusterIndex:"
- "sharedApplication"
- "v24@0:8q16"
```
