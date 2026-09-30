## CoreCDP

> `/System/Library/PrivateFrameworks/CoreCDP.framework/CoreCDP`

```diff

-416.125.2.0.0
-  __TEXT.__text: 0x4ec70
+416.125.6.0.0
+  __TEXT.__text: 0x4ed08
   __TEXT.__auth_stubs: 0x1040
   __TEXT.__objc_methlist: 0x3714
-  __TEXT.__const: 0x1304
+  __TEXT.__const: 0x1324
   __TEXT.__gcc_except_tab: 0x1174
-  __TEXT.__oslogstring: 0x856e
+  __TEXT.__oslogstring: 0x8626
   __TEXT.__cstring: 0x5684
   __TEXT.__dlopen_cstrs: 0x68
   __TEXT.__ustring: 0x28
-  __TEXT.__unwind_info: 0x14a0
+  __TEXT.__unwind_info: 0x14a8
   __TEXT.__objc_classname: 0x718
   __TEXT.__objc_methname: 0x88b1
   __TEXT.__objc_methtype: 0x1a3d

   - /usr/lib/libMobileGestalt.dylib
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 639B24A6-9592-3A34-8364-791D3E476B6F
+  UUID: 7F2AF795-0C9B-3470-A57E-1A374F1640BA
   Functions: 2203
-  Symbols:   7371
-  CStrings:  3550
+  Symbols:   7367
+  CStrings:  3551
 
CStrings:
+ "%@: Returning cached 'silentEscrowRecordRepairEnabled' value (%@) from account (%{sensitive}@)"
+ "%@: Unable to generate context for account (%{sensitive}@) with no DSID"
+ "Asking security to create custodian recovery key for %{sensitive}@"
+ "Asking security to delete custodian recovery key for %{sensitive}@"
+ "Attempting to finish secure terms flow for %{sensitive}@ with type %ld"
+ "Failed to find account for appleID: %{sensitive}@"
+ "Obtaining recovery key from security for custodian recovery with UUID: %{sensitive}@"
+ "Something went wrong... (%@) could not find a stashed token for primary Account: <%{sensitive}@ : %{sensitive}@>"
+ "Starting MRK verification for %{sensitive}@"
- "%@: Returning cached 'silentEscrowRecordRepairEnabled' value (%@) from account (%@)"
- "%@: Unable to generate context for account (%@) with no DSID"
- "Asking security to create custodian recovery key for %@"
- "Asking security to delete custodian recovery key for %@"
- "Attempting to finish secure terms flow for %@ with type %ld"
- "Failed to find account for appleID: %@"
- "Something went wrong... (%@) could not find a stashed token for primary Account: <%@ : %@>"
- "Starting MRK verification for %@"

```
