## ComputeSafeguards

> `/System/Library/PrivateFrameworks/ComputeSafeguards.framework/ComputeSafeguards`

```diff

-2964.60.10.0.0
-  __TEXT.__text: 0x30040
+2964.60.14.0.0
+  __TEXT.__text: 0x30068
   __TEXT.__auth_stubs: 0x740
   __TEXT.__objc_methlist: 0x27e4
   __TEXT.__const: 0x260

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
   - /usr/lib/libspindump.dylib
-  UUID: E59BD2C6-204B-391B-8A2A-7093A1F383D2
+  UUID: 31867474-1F6F-343C-9E82-A9D2A7FDF3B1
   Functions: 1170
-  Symbols:   3620
+  Symbols:   3621
   CStrings:  2652
 
Symbols:
+ ___chkstk_darwin
Functions:
~ -[CSMitigationManager getProcessPathForPID:] : 264 -> 284
~ -[CSProcessManager fullProcessNameForPid:] : 200 -> 220

```
