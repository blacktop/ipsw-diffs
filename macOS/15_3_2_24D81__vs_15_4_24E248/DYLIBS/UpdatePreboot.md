## UpdatePreboot

> `/System/Library/PrivateFrameworks/UpdatePreboot.framework/Versions/A/UpdatePreboot`

```diff

-934.81.1.0.0
-  __TEXT.__text: 0xf474
+934.100.30.0.0
+  __TEXT.__text: 0xfc20
   __TEXT.__auth_stubs: 0x2d0
   __TEXT.__objc_methlist: 0x17c
   __TEXT.__const: 0x60

   - /System/Library/PrivateFrameworks/APFS.framework/Versions/A/APFS
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 1FC93F11-7EDA-3287-8753-FA3412714DD2
+  UUID: 4142C933-355D-3B40-B3CD-A6F35BB8C492
   Functions: 34
   Symbols:   196
   CStrings:  1035
Functions:
~ +[UpdatePreboot calcUpdatePrebootLockAcquireForMP:forSD:cwdFD:flockFD:] : 1092 -> 1116
~ +[UpdatePreboot calcUpdatePrebootLockReleaseForCWDFD:forFLOCKFD:] : 764 -> 788
~ +[UpdatePreboot calcMountPointForDisk:mountPoint:] : 252 -> 244
~ +[UpdatePreboot copyFileFromPath:toDirAtPath:newName:interimDirs:recursive:preDelete:flags:copyFileErr:] : 996 -> 1012
~ _copyFileFromPath_callback : 204 -> 208
~ +[UpdatePreboot backerOuterBeginForSubjectDir:tmpFilePath:] : 1072 -> 1088
~ +[UpdatePreboot backerOuterEndForError:forSubjectDir:forTmpFilePath:] : 1532 -> 1572
~ +[UpdatePreboot copyIfExistsFromPath:toDirAtPath:abortOnErr:didTry:setErrIfErr:shouldAbort:] : 768 -> 792
~ +[UpdatePreboot addOrModifyUsersForDisk:doOnlyUser:useExistingAdminInfo:usersAndAttributes:adminUsers:] : 33672 -> 34292
~ +[UpdatePreboot modifyAdminGroupForDisk:adminUsers:removeUserFromAdmin:addUserToAdmin:] : 7660 -> 8244
~ +[UpdatePreboot deleteUserForDisk:user:] : 9684 -> 10304

```
