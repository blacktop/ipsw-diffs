## CallKit

> `/System/Library/Frameworks/CallKit.framework/CallKit`

```diff

-1364.100.4.0.0
+1367.100.1.0.0
   __TEXT.__text: 0x67ba0
   __TEXT.__auth_stubs: 0x940
   __TEXT.__objc_methlist: 0x8fd4
   __TEXT.__const: 0x120
-  __TEXT.__cstring: 0x6250
+  __TEXT.__cstring: 0x6258
   __TEXT.__oslogstring: 0x3694
   __TEXT.__gcc_except_tab: 0x778
   __TEXT.__unwind_info: 0x1ca0
   __TEXT.__objc_classname: 0x1471
-  __TEXT.__objc_methname: 0x119e2
-  __TEXT.__objc_methtype: 0x3df4
+  __TEXT.__objc_methname: 0x119f7
+  __TEXT.__objc_methtype: 0x3de8
   __TEXT.__objc_stubs: 0xaa00
   __DATA_CONST.__got: 0x4e0
   __DATA_CONST.__const: 0xd40

   __AUTH_CONST.__objc_const: 0xebf0
   __AUTH_CONST.__objc_intobj: 0x60
   __AUTH_CONST.__objc_arrayobj: 0x48
-  __AUTH.__objc_data: 0x19a0
+  __AUTH.__objc_data: 0x1c20
   __DATA.__objc_ivar: 0x920
   __DATA.__data: 0x1740
   __DATA.__bss: 0x110
-  __DATA_DIRTY.__objc_data: 0xdc0
+  __DATA_DIRTY.__objc_data: 0xb40
   __DATA_DIRTY.__bss: 0x70
   - /System/Library/Frameworks/AVFAudio.framework/AVFAudio
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libsqlite3.dylib
-  UUID: 3DF7A23F-5014-35B9-9C23-EFDC8646B913
+  UUID: BC0ED0BE-B3B6-3340-857D-FD3D1DE08063
   Functions: 3177
   Symbols:   10388
-  CStrings:  4683
+  CStrings:  4682
 
Symbols:
+ -[CXSetTranslatingCallAction fulfillUsingTranslationEngine:]
+ -[CXSetTranslatingCallAction initWithCallUUID:isTranslating:isSystemInitiated:localLanguage:remoteLanguage:]
+ -[CXSetTranslatingCallAction initWithCallUUID:isTranslating:localLanguage:remoteLanguage:]
+ -[CXSetTranslatingCallAction localLanguage]
+ -[CXSetTranslatingCallAction remoteLanguage]
+ _OBJC_IVAR_$_CXSetTranslatingCallAction._localLanguage
+ _OBJC_IVAR_$_CXSetTranslatingCallAction._remoteLanguage
+ _objc_msgSend$localLanguage
+ _objc_msgSend$remoteLanguage
- -[CXSetTranslatingCallAction fulfillWithTranslationEngine:]
- -[CXSetTranslatingCallAction initWithCallUUID:isTranslating:isSystemInitiated:localLocale:remoteLocale:]
- -[CXSetTranslatingCallAction initWithCallUUID:isTranslating:localLocale:remoteLocale:]
- -[CXSetTranslatingCallAction localLocale]
- -[CXSetTranslatingCallAction remoteLocale]
- _OBJC_IVAR_$_CXSetTranslatingCallAction._localLocale
- _OBJC_IVAR_$_CXSetTranslatingCallAction._remoteLocale
- _objc_msgSend$localLocale
- _objc_msgSend$remoteLocale
CStrings:
+ " localLanguage=%@"
+ " remoteLanguage=%@"
+ "T@\"NSString\",R,N,V_localLanguage"
+ "T@\"NSString\",R,N,V_remoteLanguage"
+ "Tq,R,N,V_translationEngine"
+ "_localLanguage"
+ "_remoteLanguage"
+ "fulfillUsingTranslationEngine:"
+ "initWithCallUUID:isTranslating:isSystemInitiated:localLanguage:remoteLanguage:"
+ "initWithCallUUID:isTranslating:localLanguage:remoteLanguage:"
+ "localLanguage"
+ "remoteLanguage"
- " localLocale=%@"
- " remoteLocale=%@"
- "@\"NSLocale\""
- "T@\"NSLocale\",R,N,V_localLocale"
- "T@\"NSLocale\",R,N,V_remoteLocale"
- "TQ,R,N,V_translationEngine"
- "_localLocale"
- "_remoteLocale"
- "fulfillWithTranslationEngine:"
- "initWithCallUUID:isTranslating:isSystemInitiated:localLocale:remoteLocale:"
- "initWithCallUUID:isTranslating:localLocale:remoteLocale:"
- "localLocale"
- "remoteLocale"

```
