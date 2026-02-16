## DASubCal

> `/System/Library/PrivateFrameworks/DataAccess.framework/Frameworks/DASubCal.framework/DASubCal`

```diff

-2691.2.2.0.0
-  __TEXT.__text: 0x879c
-  __TEXT.__auth_stubs: 0x470
+2691.4.5.0.0
+  __TEXT.__text: 0x91bc
+  __TEXT.__auth_stubs: 0x410
   __TEXT.__objc_methlist: 0xce8
   __TEXT.__const: 0x58
   __TEXT.__cstring: 0x52a
   __TEXT.__oslogstring: 0x94b
-  __TEXT.__unwind_info: 0x238
+  __TEXT.__unwind_info: 0x2a8
   __TEXT.__objc_classname: 0x17a
   __TEXT.__objc_methname: 0x2b07
   __TEXT.__objc_methtype: 0xb30

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0xca8
   __DATA_CONST.__objc_superrefs: 0x10
-  __AUTH_CONST.__auth_got: 0x240
+  __AUTH_CONST.__auth_got: 0x210
   __AUTH_CONST.__const: 0x40
   __AUTH_CONST.__cfstring: 0x820
   __AUTH_CONST.__objc_const: 0x1978

   - /System/Library/PrivateFrameworks/iCalendar.framework/iCalendar
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: 478ADD87-9E3A-3953-B5F6-F3AB8FD16C0E
+  UUID: 60EAEFE3-7C5B-3D0A-9BEE-771E64724303
   Functions: 219
-  Symbols:   1043
+  Symbols:   1037
   CStrings:  811
 
Symbols:
+ _objc_retainAutoreleasedReturnValue
- _objc_claimAutoreleasedReturnValue
- _objc_retainAutoreleaseReturnValue
- _objc_retain_x1
- _objc_retain_x25
- _objc_retain_x28
- _objc_retain_x4
- _objc_retain_x8
Functions:
~ -[SubCalAccount initWithBackingAccountInfo:] : 224 -> 232
~ ___44-[SubCalAccount initWithBackingAccountInfo:]_block_invoke : 72 -> 76
~ -[SubCalAccount accountDescription] : 188 -> 208
~ -[SubCalAccount setAccountDescription:] : 176 -> 188
~ -[SubCalAccount subscriptionURL] : 516 -> 572
~ -[SubCalAccount calDAVURLPath] : 88 -> 96
~ -[SubCalAccount setCalDAVURLPath:] : 140 -> 148
~ -[SubCalAccount calendarExternalId] : 160 -> 176
~ -[SubCalAccount taskManager] : 108 -> 124
~ -[SubCalAccount _checkValidityWithConsumer:quickValidate:] : 340 -> 360
~ -[SubCalAccount subCalValidationTask:finishedWithError:calendarName:document:calendarData:] : 364 -> 380
~ -[SubCalAccount _tmpICSCalendarPath] : 108 -> 116
~ -[SubCalAccount saveTmpICSData] : 116 -> 120
~ -[SubCalAccount tmpICSData] : 184 -> 200
~ -[SubCalAccount clearTmpICSData] : 324 -> 336
~ -[SubCalAccount allowInsecureConnection] : 76 -> 80
~ -[SubCalAccount setAllowInsecureConnection:] : 100 -> 104
~ -[SubCalAccount upgradeAccount] : 1252 -> 1364
~ -[SubCalAccount upgradeAccountSpecificPropertiesOnAccount:inStore:parentAccount:] : 472 -> 492
~ -[SubCalAccount setHost:] : 452 -> 472
~ -[SubCalAccount refreshInterval] : 76 -> 80
~ -[SubCalAccount setRefreshInterval:] : 104 -> 108
~ -[SubCalAccount isManagedCalendar] : 68 -> 72
~ -[SubCalAccount isChinaHolidayCalendar] : 104 -> 116
~ -[SubCalAccount isSyncedHolidayCalendar] : 204 -> 228
~ -[SubCalAccount isHolidaySubscribedCalendar] : 108 -> 120
~ -[SubCalAccount isEqualToAccount:] : 588 -> 640
~ -[SubCalAccount accountHasSignificantPropertyChangesWithChangeInfo:] : 348 -> 380
~ -[SubCalAccount removeDBSyncDataForAccountChange:] : 560 -> 580
~ -[SubCalAccount removeDataFromCalendar:forAccountChange:] : 1552 -> 1600
~ -[SubCalAccount localizedIdenticalAccountFailureMessage] : 128 -> 136
~ -[SubCalAccount localizedInvalidPasswordMessage] : 204 -> 220
~ -[SubCalAccount onBehalfOfBundleIdentifier] : 16 -> 64
~ -[SubCalAccount hasSubscribedCalendarAtURL:] : 88 -> 92
~ -[SubCalAccount setTmpICSData:] : 20 -> 72
~ -[NSError(SubCalValidity) isSubCalAuthError] : 96 -> 100
~ _subCalExternalRep : 88 -> 96
~ __subCalLegacyDigestForCalendar : 140 -> 148
~ __subCalLegacySetDigestOnCalendar : 156 -> 160
~ _subCalDigestForCalendar : 168 -> 176
~ _subCalRefreshFlagsForCalendar : 68 -> 72
~ _subCalSetRefreshFlagsOnCalendar : 148 -> 160
~ +[SubCalLocalDBHelper initializeSourceWithExternalId:inStore:needsSave:error:] : 204 -> 220
~ +[SubCalLocalDBHelper initializeCalendarWithExternalId:inSource:needsSave:error:] : 536 -> 560
~ +[SubCalLocalDBHelper _existingCalendarInCalDAVSourceWithExternalID:inSource:] : 528 -> 540
~ +[SubCalLocalDBHelper _relativePathFromCalDAVExternalID:] : 84 -> 92
~ +[SubCalLocalDBHelper _makeCalendarWithExternalId:inStore:error:] : 148 -> 152
~ -[NSString(SubCalUtilities) isSubCalURLString] : 244 -> 256
~ -[NSString(SubCalDigest) modTagForSubCal] : 276 -> 284
~ -[NSError(SubCalTaskReachabilityError) isSubCalReachabilityError] : 108 -> 112
~ _SubCalCopySaveAccountNotification : 464 -> 504
~ __SubCalCopyAccountNotification : 276 -> 264
~ _SubCalCopyInvalidAccountNotification : 652 -> 724
~ _SubCalCopyAuthNeededForHostNotification : 1172 -> 1208
~ _SubCalCopyWhereToAccountNotification : 396 -> 428
~ _SubCalCopyDuplicateAccountNotification : 276 -> 296
~ _SubCalCopySSLFailureNotification : 476 -> 520
~ -[SubCalURLRequest initWithURL:wasUserRequested:] : 168 -> 160
~ -[SubCalURLRequest _setHeadersOnRequest:] : 620 -> 640
~ -[SubCalURLRequest _markEndTime] : 184 -> 200
~ -[SubCalURLRequest _idleTimerFired] : 568 -> 604
~ -[SubCalURLRequest _createIdleTimer] : 172 -> 176
~ -[SubCalURLRequest _extendIdleTimer] : 112 -> 120
~ -[SubCalURLRequest _cancelIdleTimer] : 168 -> 176
~ -[SubCalURLRequest startConnection] : 652 -> 684
~ -[SubCalURLRequest cancel] : 420 -> 444
~ -[SubCalURLRequest _finishWithError:] : 392 -> 420
~ -[SubCalURLRequest URLSession:didBecomeInvalidWithError:] : 188 -> 192
~ -[SubCalURLRequest URLSession:didReceiveChallenge:completionHandler:] : 212 -> 204
~ -[SubCalURLRequest URLSession:task:didReceiveChallenge:completionHandler:] : 196 -> 188
~ -[SubCalURLRequest URLSession:task:willPerformHTTPRedirection:newRequest:completionHandler:] : 344 -> 304
~ ___92-[SubCalURLRequest URLSession:task:willPerformHTTPRedirection:newRequest:completionHandler:]_block_invoke : 1200 -> 1272
~ ___57-[SubCalURLRequest URLSession:task:didCompleteWithError:]_block_invoke : 648 -> 680
~ -[SubCalURLRequest URLSession:dataTask:didReceiveResponse:completionHandler:] : 212 -> 204
~ ___77-[SubCalURLRequest URLSession:dataTask:didReceiveResponse:completionHandler:]_block_invoke : 772 -> 792
~ ___55-[SubCalURLRequest URLSession:dataTask:didReceiveData:]_block_invoke : 300 -> 316
~ -[SubCalURLRequest _canAuthenticateAgainstProtectionSpace:] : 348 -> 356
~ -[SubCalURLRequest _respondToChallenge:withCredential:noCredentialBehavior:completionHandler:] : 472 -> 468
~ -[SubCalURLRequest _handleAuthenticationChallenge:completionHandler:] : 972 -> 1008
~ ___69-[SubCalURLRequest _handleAuthenticationChallenge:completionHandler:]_block_invoke : 204 -> 208
~ -[SubCalURLRequest _openFileHandle] : 472 -> 488
~ -[SubCalURLRequest _receivedDataForFile:] : 744 -> 796
~ +[SubCalURLRequest _cachedICSFilesDirectory] : 68 -> 84
~ ___44+[SubCalURLRequest _cachedICSFilesDirectory]_block_invoke : 144 -> 156
~ ___40+[SubCalURLRequest _initializeFileCache]_block_invoke : 984 -> 1020
~ -[SubCalURLRequest setFilePath:] : 12 -> 64
~ -[SubCalURLRequest setStatusReport:] : 12 -> 64
~ -[SubCalURLRequest setSession:] : 12 -> 64
~ -[SubCalURLRequest setTask:] : 12 -> 64
~ -[SubCalURLRequest setConnectionData:] : 12 -> 64
~ -[SubCalURLRequest setFileHandle:] : 12 -> 64
~ -[SubCalURLRequest setStartTime:] : 12 -> 64
~ -[SubCalURLRequest setIdleTimer:] : 12 -> 64
~ -[SubCalURLRequest setStartRunloopDescriptionString:] : 12 -> 64
~ -[SubCalDATask cancelTaskWithReason:underlyingError:] : 224 -> 232
~ -[SubCalDATask finishWithError:] : 144 -> 148
~ -[SubCalDATask setStatusReport:] : 12 -> 64
~ -[SubCalValidationTask willFinish] : 76 -> 80
~ -[SubCalValidationTask performDelegateCallbackWithError:] : 192 -> 208
~ -[SubCalValidationTask performTask] : 500 -> 552
~ -[SubCalValidationTask handleTrustChallenge:forSubCalURLRequest:] : 100 -> 104
~ -[SubCalValidationTask subCalURLRequest:finishedWithData:error:] : 348 -> 360
~ -[SubCalValidationTask _stringBeforeNewline:length:] : 180 -> 188
~ -[SubCalValidationTask _searchForCalNameInConnectionData:] : 324 -> 332
~ -[SubCalValidationTask _tryQuickValidationCurrentData:] : 508 -> 524
~ -[SubCalValidationTask setSubscriptionURL:] : 20 -> 80
~ -[SubCalValidationTask setUsername:] : 20 -> 80
~ -[SubCalValidationTask setPassword:] : 20 -> 80
~ -[SubCalValidationTask setRequest:] : 20 -> 80
~ -[SubCalValidationTask setIcsData:] : 20 -> 80
~ -[SubCalValidationTask setIcsDocument:] : 20 -> 80
~ -[SubCalValidationTask setCalendarName:] : 20 -> 80
~ -[SubCalURLRequest initWithURL:wasUserRequested:].cold.1 : 100 -> 104

```
