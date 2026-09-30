## SiriCore

> `/System/Library/PrivateFrameworks/SiriCore.framework/SiriCore`

```diff

-3400.19.1.0.0
-  __TEXT.__text: 0x34734
+3401.3.1.0.0
+  __TEXT.__text: 0x34e40
   __TEXT.__auth_stubs: 0x13c0
-  __TEXT.__objc_methlist: 0x3378
-  __TEXT.__const: 0xb4
+  __TEXT.__objc_methlist: 0x33f8
+  __TEXT.__const: 0xc4
   __TEXT.__gcc_except_tab: 0x268
-  __TEXT.__cstring: 0x5842
-  __TEXT.__oslogstring: 0x2b0c
-  __TEXT.__unwind_info: 0xb10
+  __TEXT.__cstring: 0x591d
+  __TEXT.__oslogstring: 0x2be0
+  __TEXT.__unwind_info: 0xb28
   __TEXT.__objc_classname: 0x86b
-  __TEXT.__objc_methname: 0x9f36
-  __TEXT.__objc_methtype: 0x1c4a
-  __TEXT.__objc_stubs: 0x6d80
-  __DATA_CONST.__got: 0x5a8
-  __DATA_CONST.__const: 0xeb0
+  __TEXT.__objc_methname: 0xa128
+  __TEXT.__objc_methtype: 0x1c54
+  __TEXT.__objc_stubs: 0x6e40
+  __DATA_CONST.__got: 0x5b8
+  __DATA_CONST.__const: 0xed8
   __DATA_CONST.__objc_classlist: 0x180
-  __DATA_CONST.__objc_catlist: 0xf0
+  __DATA_CONST.__objc_catlist: 0xf8
   __DATA_CONST.__objc_protolist: 0x88
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x2260
+  __DATA_CONST.__objc_selrefs: 0x22b8
   __DATA_CONST.__objc_superrefs: 0x128
   __AUTH_CONST.__auth_got: 0x9f0
   __AUTH_CONST.__const: 0x200
   __AUTH_CONST.__cfstring: 0x3960
-  __AUTH_CONST.__objc_const: 0x8598
+  __AUTH_CONST.__objc_const: 0x8678
   __AUTH_CONST.__objc_intobj: 0x108
   __AUTH_CONST.__objc_doubleobj: 0x10
   __AUTH.__objc_data: 0x280
   __AUTH.__data: 0x10
-  __DATA.__objc_ivar: 0x630
+  __DATA.__objc_ivar: 0x63c
   __DATA.__data: 0x660
-  __DATA.__bss: 0x40
+  __DATA.__bss: 0x58
   __DATA_DIRTY.__objc_data: 0xc80
-  __DATA_DIRTY.__bss: 0x68
+  __DATA_DIRTY.__bss: 0x50
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork
   - /System/Library/Frameworks/Contacts.framework/Contacts
   - /System/Library/Frameworks/CoreFoundation.framework/CoreFoundation

   - /usr/lib/libresolv.9.dylib
   - /usr/lib/libsqlite3.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 1254
-  Symbols:   1860
-  CStrings:  2976
+  Functions: 1265
+  Symbols:   1873
+  CStrings:  3001
 
Symbols:
+ _kSymptomDiagnosticReplySuccess
+ _OBJC_CLASS_$_NSLock
CStrings:
+ "%!s(MISSING) invalid type for ABC"
+ "%!s(MISSING) Type cannot be nil for ABC"
+ "keysAcceptedWithTimestamp"
+ "%!s(MISSING) %!@(MISSING) key was rejected less than an hour ago. Will skip reporting."
+ "lock"
+ "_keysRejectedWithTimestamp"
+ "timeIntervalSinceDate:"
+ "setLock:"
+ "siriCore_isWithin24HourInterval"
+ "reportIssueWithBackOffTimerForType:subType:context:processIdentifier:walkboutStatus:"
+ "setKeysRejectedWithTimestamp:"
+ "-[SiriCoreSymptomsReporter reportIssueForType:subType:context:processIdentifier:walkboutStatus:withPcap:]"
+ "T@\"NSLock\",&,N,V_lock"
+ "unlock"
+ "%!s(MISSING) reporting issue for type: %!@(MISSING)"
+ "@\"NSLock\""
+ "_lock"
+ "-[SiriCoreSymptomsReporter reportIssueWithBackOffTimerForType:subType:context:processIdentifier:walkboutStatus:]"
+ "T@\"NSMutableDictionary\",&,N,V_keysAcceptedWithTimestamp"
+ "T@\"NSMutableDictionary\",&,N,V_keysRejectedWithTimestamp"
+ "keysRejectedWithTimestamp"
+ "setKeysAcceptedWithTimestamp:"
+ "_keysAcceptedWithTimestamp"
+ "%!s(MISSING) %!@(MISSING) key was already accepted today. Will skip reporting."
+ "siriCore_isWithin1HourInterval"

```
