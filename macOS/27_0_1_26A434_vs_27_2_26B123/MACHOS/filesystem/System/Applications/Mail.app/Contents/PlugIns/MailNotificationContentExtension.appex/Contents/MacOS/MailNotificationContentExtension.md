## MailNotificationContentExtension

> `/System/Applications/Mail.app/Contents/PlugIns/MailNotificationContentExtension.appex/Contents/MacOS/MailNotificationContentExtension`

### Sections with Same Size but Changed Content

- `__TEXT.__gcc_except_tab`
- `__TEXT.__objc_classname`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__objc_classlist`
- `__DATA_CONST.__objc_protolist`
- `__DATA_CONST.__objc_protorefs`
- `__DATA_CONST.__objc_superrefs`
- `__DATA_CONST.__objc_intobj`
- `__DATA_CONST.__objc_floatobj`
- `__DATA_CONST.__objc_arraydata`
- `__DATA_CONST.__objc_dictobj`
- `__DATA.__objc_const`
- `__DATA.__objc_ivar`
- `__DATA.__objc_data`
- `__DATA.__data`

```diff

-3901.100.1.1.12
-  __TEXT.__text: 0xba44
-  __TEXT.__auth_stubs: 0x400
-  __TEXT.__objc_stubs: 0x3600
-  __TEXT.__objc_methlist: 0xed4
-  __TEXT.__const: 0x68
+3901.200.71.1.16
+  __TEXT.__text: 0xc034
+  __TEXT.__auth_stubs: 0x410
+  __TEXT.__objc_stubs: 0x3800
+  __TEXT.__objc_methlist: 0xf44
+  __TEXT.__const: 0x6c
   __TEXT.__gcc_except_tab: 0xb0
-  __TEXT.__cstring: 0x990
-  __TEXT.__objc_methname: 0x4117
-  __TEXT.__oslogstring: 0x6a0
+  __TEXT.__cstring: 0x99f
+  __TEXT.__objc_methname: 0x4334
+  __TEXT.__oslogstring: 0x771
   __TEXT.__objc_classname: 0x1a7
-  __TEXT.__objc_methtype: 0x13c4
-  __TEXT.__unwind_info: 0x430
-  __DATA_CONST.__const: 0x4b0
+  __TEXT.__objc_methtype: 0x142f
+  __TEXT.__unwind_info: 0x460
+  __DATA_CONST.__const: 0x4d0
   __DATA_CONST.__cfstring: 0x7a0
   __DATA_CONST.__objc_classlist: 0x58
   __DATA_CONST.__objc_protolist: 0x58
   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_protorefs: 0x8
   __DATA_CONST.__objc_superrefs: 0x58
-  __DATA_CONST.__objc_intobj: 0x30
   __DATA_CONST.__objc_floatobj: 0x10
   __DATA_CONST.__objc_arraydata: 0x10
   __DATA_CONST.__objc_dictobj: 0x28
-  __DATA_CONST.__auth_got: 0x210
-  __DATA_CONST.__got: 0x368
+  __DATA_CONST.__objc_intobj: 0x30
+  __DATA_CONST.__auth_got: 0x218
+  __DATA_CONST.__got: 0x380
   __DATA.__objc_const: 0x1e40
-  __DATA.__objc_selrefs: 0x1288
+  __DATA.__objc_selrefs: 0x1300
   __DATA.__objc_ivar: 0xb4
   __DATA.__objc_data: 0x370
   __DATA.__data: 0x430
-  __DATA.__bss: 0x41
+  __DATA.__bss: 0x58
   - /System/Library/Frameworks/AppKit.framework/Versions/C/AppKit
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation
   - /System/Library/Frameworks/CoreServices.framework/Versions/A/CoreServices

   - /System/Library/PrivateFrameworks/Synapse.framework/Versions/A/Synapse
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  Functions: 275
-  Symbols:   232
-  CStrings:  963
+  Functions: 286
+  Symbols:   236
+  CStrings:  982
 
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
