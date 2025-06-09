## POP

> `/System/Library/PrivateFrameworks/Message.framework/MailServices/POP.framework/POP`

```diff

-3826.600.51.2.1
-  __TEXT.__text: 0x8c34
+3853.100.6.2.6
+  __TEXT.__text: 0x8c64
   __TEXT.__auth_stubs: 0x4a0
   __TEXT.__objc_methlist: 0x76c
-  __TEXT.__gcc_except_tab: 0x14d4
+  __TEXT.__gcc_except_tab: 0x14cc
   __TEXT.__cstring: 0x3eb
   __TEXT.__ustring: 0x2fc
   __TEXT.__const: 0xa8

   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libc++.1.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 7734322C-CF41-3D88-9876-1F8FD056882E
+  UUID: 585D22E3-7EC8-3BD1-909F-69FE8BB9D47D
   Functions: 156
   Symbols:   910
   CStrings:  570
Functions:
~ -[MFLibraryPOPStore _fetchBodyDataForMessage:andHeaderDataIfReadilyAvailable:downloadIfNecessary:partial:] : 1064 -> 1084
~ +[MFPOP3Fetcher _fetchWithAccount:intoQueue:newMessages:oldMessages:preservingUID:withStore:] : 4556 -> 4572
~ -[MFPOP3Connection _getStatusFromReply] : 1208 -> 1220

```
