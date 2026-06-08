## DASubCal

> `/System/Library/PrivateFrameworks/DataAccess.framework/Frameworks/DASubCal.framework/DASubCal`

```diff

-2691.4.6.0.0
-  __TEXT.__text: 0x91bc
-  __TEXT.__auth_stubs: 0x410
+2703.0.0.0.0
+  __TEXT.__text: 0x8504
   __TEXT.__objc_methlist: 0xce8
   __TEXT.__const: 0x58
-  __TEXT.__cstring: 0x52a
+  __TEXT.__cstring: 0x535
   __TEXT.__oslogstring: 0x94b
-  __TEXT.__unwind_info: 0x2a8
-  __TEXT.__objc_classname: 0x17a
-  __TEXT.__objc_methname: 0x2b07
-  __TEXT.__objc_methtype: 0xb30
-  __TEXT.__objc_stubs: 0x2720
-  __DATA_CONST.__got: 0x230
+  __TEXT.__unwind_info: 0x238
+  __TEXT.__objc_stubs: 0x0
+  __TEXT.__auth_stubs: 0x0
+  __TEXT.__objc_classname: 0x0
+  __TEXT.__objc_methname: 0x0
+  __TEXT.__objc_methtype: 0x0
   __DATA_CONST.__const: 0x1f0
   __DATA_CONST.__objc_classlist: 0x28
   __DATA_CONST.__objc_catlist: 0x10

   __DATA_CONST.__objc_imageinfo: 0x8
   __DATA_CONST.__objc_selrefs: 0xca8
   __DATA_CONST.__objc_superrefs: 0x10
-  __AUTH_CONST.__auth_got: 0x210
+  __DATA_CONST.__got: 0x230
   __AUTH_CONST.__const: 0x40
   __AUTH_CONST.__cfstring: 0x820
   __AUTH_CONST.__objc_const: 0x1978
   __AUTH_CONST.__objc_intobj: 0x30
-  __AUTH.__objc_data: 0xa0
+  __AUTH_CONST.__auth_got: 0x0
+  __AUTH.__objc_data: 0x50
   __DATA.__objc_ivar: 0xa0
   __DATA.__data: 0x360
   __DATA.__bss: 0x18
-  __DATA_DIRTY.__objc_data: 0xf0
+  __DATA_DIRTY.__objc_data: 0x140
   __DATA_DIRTY.__bss: 0x8
   - /System/Library/Frameworks/Accounts.framework/Accounts
   - /System/Library/Frameworks/CFNetwork.framework/CFNetwork

   - /System/Library/PrivateFrameworks/iCalendar.framework/iCalendar
   - /usr/lib/libSystem.B.dylib
   - /usr/lib/libobjc.A.dylib
-  UUID: D56BD10F-9FA4-3553-B4AE-844C25876220
+  UUID: 3C2380F4-AA4A-3D10-9742-4BEB847AD62D
   Functions: 219
-  Symbols:   1037
-  CStrings:  811
+  Symbols:   1042
+  CStrings:  207
 
Symbols:
+ _objc_claimAutoreleasedReturnValue
+ _objc_retainAutoreleaseReturnValue
+ _objc_retain_x1
+ _objc_retain_x25
+ _objc_retain_x28
+ _objc_retain_x4
+ _objc_retain_x8
- _objc_retainAutoreleasedReturnValue
- _objc_retain_x24
Functions:
~ -[SubCalAccount initWithBackingAccountInfo:] : 232 -> 224
~ ___44-[SubCalAccount initWithBackingAccountInfo:]_block_invoke : 76 -> 72
~ -[SubCalAccount accountDescription] : 208 -> 188
~ -[SubCalAccount setAccountDescription:] : 188 -> 176
~ -[SubCalAccount subscriptionURL] : 572 -> 516
~ -[SubCalAccount calDAVURLPath] : 96 -> 88
~ -[SubCalAccount setCalDAVURLPath:] : 148 -> 140
~ -[SubCalAccount calendarExternalId] : 176 -> 160
~ -[SubCalAccount taskManager] : 124 -> 112
~ -[SubCalAccount _checkValidityWithConsumer:quickValidate:] : 360 -> 340
~ -[SubCalAccount subCalValidationTask:finishedWithError:calendarName:document:calendarData:] : 380 -> 364
~ -[SubCalAccount _tmpICSCalendarPath] : 116 -> 108
~ -[SubCalAccount tmpICSData] : 200 -> 188
~ -[SubCalAccount clearTmpICSData] : 336 -> 280
~ -[SubCalAccount allowInsecureConnection] : 80 -> 76
~ -[SubCalAccount setAllowInsecureConnection:] : 104 -> 100
~ -[SubCalAccount upgradeAccount] : 1364 -> 1208
~ -[SubCalAccount upgradeAccountSpecificPropertiesOnAccount:inStore:parentAccount:] : 492 -> 476
~ -[SubCalAccount setHost:] : 472 -> 448
~ -[SubCalAccount refreshInterval] : 80 -> 76
~ -[SubCalAccount setRefreshInterval:] : 108 -> 104
~ -[SubCalAccount isManagedCalendar] : 72 -> 68
~ -[SubCalAccount isChinaHolidayCalendar] : 116 -> 104
~ -[SubCalAccount isSyncedHolidayCalendar] : 228 -> 204
~ -[SubCalAccount isHolidaySubscribedCalendar] : 120 -> 108
~ -[SubCalAccount isEqualToAccount:] : 640 -> 588
~ -[SubCalAccount accountHasSignificantPropertyChangesWithChangeInfo:] : 380 -> 348
~ -[SubCalAccount removeDBSyncDataForAccountChange:] : 580 -> 564
~ -[SubCalAccount removeDataFromCalendar:forAccountChange:] : 1600 -> 1548
~ -[SubCalAccount localizedIdenticalAccountFailureMessage] : 136 -> 128
~ -[SubCalAccount localizedInvalidPasswordMessage] : 220 -> 204
~ -[SubCalAccount onBehalfOfBundleIdentifier] : 64 -> 16
~ -[SubCalAccount hasSubscribedCalendarAtURL:] : 92 -> 88
~ -[SubCalAccount setIsManagedCalendar:] : 16 -> 20
~ -[SubCalAccount subCalAccountVersion] : 16 -> 20
~ -[SubCalAccount setSubCalAccountVersion:] : 16 -> 20
~ -[SubCalAccount setTmpICSData:] : 72 -> 20
~ -[NSError(SubCalValidity) isSubCalAuthError] : 100 -> 96
~ _subCalExternalRep : 96 -> 88
~ __subCalLegacyDigestForCalendar : 148 -> 140
~ __subCalLegacySetDigestOnCalendar : 160 -> 156
~ _subCalDigestForCalendar : 176 -> 152
~ _subCalRefreshFlagsForCalendar : 72 -> 68
~ _subCalSetRefreshFlagsOnCalendar : 160 -> 148
~ +[SubCalLocalDBHelper initializeSourceWithExternalId:inStore:needsSave:error:] : 220 -> 204
~ +[SubCalLocalDBHelper initializeCalendarWithExternalId:inSource:needsSave:error:] : 560 -> 492
~ +[SubCalLocalDBHelper _existingCalendarInCalDAVSourceWithExternalID:inSource:] : 540 -> 532
~ +[SubCalLocalDBHelper _relativePathFromCalDAVExternalID:] : 92 -> 84
~ +[SubCalLocalDBHelper _makeCalendarWithExternalId:inStore:error:] : 152 -> 148
~ -[NSString(SubCalUtilities) isSubCalURLString] : 256 -> 244
~ -[NSString(SubCalDigest) modTagForSubCal] : 284 -> 276
~ -[NSError(SubCalTaskReachabilityError) isSubCalReachabilityError] : 112 -> 108
~ _SubCalCopySaveAccountNotification : 504 -> 464
~ __SubCalCopyAccountNotification : 264 -> 276
~ _SubCalCopyInvalidAccountNotification : 724 -> 652
~ _SubCalCopyAuthNeededForHostNotification : 1208 -> 1172
~ _SubCalCopyWhereToAccountNotification : 428 -> 396
~ _SubCalCopyDuplicateAccountNotification : 296 -> 276
~ _SubCalCopySSLFailureNotification : 520 -> 476
~ -[SubCalURLRequest initWithURL:wasUserRequested:] : 160 -> 168
~ -[SubCalURLRequest _setHeadersOnRequest:] : 640 -> 576
~ -[SubCalURLRequest _markEndTime] : 200 -> 184
~ -[SubCalURLRequest _idleTimerFired] : 604 -> 524
~ -[SubCalURLRequest _createIdleTimer] : 176 -> 172
~ -[SubCalURLRequest _extendIdleTimer] : 120 -> 112
~ -[SubCalURLRequest _cancelIdleTimer] : 176 -> 168
~ -[SubCalURLRequest startConnection] : 684 -> 608
~ -[SubCalURLRequest cancel] : 444 -> 376
~ -[SubCalURLRequest _finishWithError:] : 420 -> 392
~ -[SubCalURLRequest URLSession:didBecomeInvalidWithError:] : 192 -> 188
~ -[SubCalURLRequest URLSession:didReceiveChallenge:completionHandler:] : 204 -> 212
~ -[SubCalURLRequest URLSession:task:didReceiveChallenge:completionHandler:] : 188 -> 196
~ -[SubCalURLRequest URLSession:task:willPerformHTTPRedirection:newRequest:completionHandler:] : 304 -> 344
~ ___92-[SubCalURLRequest URLSession:task:willPerformHTTPRedirection:newRequest:completionHandler:]_block_invoke : 1272 -> 1108
~ ___57-[SubCalURLRequest URLSession:task:didCompleteWithError:]_block_invoke : 680 -> 604
~ -[SubCalURLRequest URLSession:dataTask:didReceiveResponse:completionHandler:] : 204 -> 212
~ ___77-[SubCalURLRequest URLSession:dataTask:didReceiveResponse:completionHandler:]_block_invoke : 792 -> 728
~ ___55-[SubCalURLRequest URLSession:dataTask:didReceiveData:]_block_invoke : 316 -> 300
~ -[SubCalURLRequest _canAuthenticateAgainstProtectionSpace:] : 356 -> 304
~ -[SubCalURLRequest _respondToChallenge:withCredential:noCredentialBehavior:completionHandler:] : 468 -> 428
~ -[SubCalURLRequest _handleAuthenticationChallenge:completionHandler:] : 1008 -> 928
~ ___69-[SubCalURLRequest _handleAuthenticationChallenge:completionHandler:]_block_invoke : 208 -> 204
~ -[SubCalURLRequest _openFileHandle] : 488 -> 428
~ -[SubCalURLRequest _receivedDataForFile:] : 796 -> 700
~ +[SubCalURLRequest _cachedICSFilesDirectory] : 84 -> 68
~ ___44+[SubCalURLRequest _cachedICSFilesDirectory]_block_invoke : 156 -> 144
~ ___40+[SubCalURLRequest _initializeFileCache]_block_invoke : 1020 -> 988
~ -[SubCalURLRequest setFilePath:] : 64 -> 12
~ -[SubCalURLRequest setStatusReport:] : 64 -> 12
~ -[SubCalURLRequest setSession:] : 64 -> 12
~ -[SubCalURLRequest setTask:] : 64 -> 12
~ -[SubCalURLRequest setConnectionData:] : 64 -> 12
~ -[SubCalURLRequest setFileHandle:] : 64 -> 12
~ -[SubCalURLRequest setStartTime:] : 64 -> 12
~ -[SubCalURLRequest setIdleTimer:] : 64 -> 12
~ -[SubCalURLRequest setStartRunloopDescriptionString:] : 64 -> 12
~ -[SubCalDATask cancelTaskWithReason:underlyingError:] : 232 -> 224
~ -[SubCalDATask finishWithError:] : 148 -> 144
~ -[SubCalDATask setStatusReport:] : 64 -> 12
~ -[SubCalValidationTask willFinish] : 80 -> 76
~ -[SubCalValidationTask performDelegateCallbackWithError:] : 208 -> 192
~ -[SubCalValidationTask performTask] : 552 -> 504
~ -[SubCalValidationTask handleTrustChallenge:forSubCalURLRequest:] : 104 -> 100
~ -[SubCalValidationTask subCalURLRequest:finishedWithData:error:] : 360 -> 348
~ -[SubCalValidationTask _stringBeforeNewline:length:] : 188 -> 180
~ -[SubCalValidationTask _searchForCalNameInConnectionData:] : 332 -> 324
~ -[SubCalValidationTask _tryQuickValidationCurrentData:] : 524 -> 464
~ -[SubCalValidationTask subscriptionURL] : 16 -> 20
~ -[SubCalValidationTask setSubscriptionURL:] : 80 -> 20
~ -[SubCalValidationTask username] : 16 -> 20
~ -[SubCalValidationTask setUsername:] : 80 -> 20
~ -[SubCalValidationTask password] : 16 -> 20
~ -[SubCalValidationTask setPassword:] : 80 -> 20
~ -[SubCalValidationTask performQuickValidation] : 16 -> 20
~ -[SubCalValidationTask setPerformQuickValidation:] : 16 -> 20
~ -[SubCalValidationTask useShortTimeout] : 16 -> 20
~ -[SubCalValidationTask setUseShortTimeout:] : 16 -> 20
~ -[SubCalValidationTask request] : 16 -> 20
~ -[SubCalValidationTask setRequest:] : 80 -> 20
~ -[SubCalValidationTask icsData] : 16 -> 20
~ -[SubCalValidationTask setIcsData:] : 80 -> 20
~ -[SubCalValidationTask icsDocument] : 16 -> 20
~ -[SubCalValidationTask setIcsDocument:] : 80 -> 20
~ -[SubCalValidationTask calendarName] : 16 -> 20
~ -[SubCalValidationTask setCalendarName:] : 80 -> 20
~ -[SubCalValidationTask foundBeginVCal] : 16 -> 20
~ -[SubCalValidationTask setFoundBeginVCal:] : 16 -> 20
~ -[SubCalValidationTask foundCalName] : 16 -> 20
~ -[SubCalValidationTask setFoundCalName:] : 16 -> 20
~ -[SubCalValidationTask searchIndex] : 16 -> 20
~ -[SubCalValidationTask setSearchIndex:] : 16 -> 20
~ -[SubCalURLRequest initWithURL:wasUserRequested:].cold.1 : 104 -> 100
CStrings:
- "#16@0:8"
- ".cxx_destruct"
- "@\"<SubCalURLRequestDelegate>\""
- "@\"<SubCalValidationTaskDelegate>\""
- "@\"DAStatusReport\""
- "@\"DATaskManager\""
- "@\"ICSDocument\""
- "@\"NSData\""
- "@\"NSDate\""
- "@\"NSFileHandle\""
- "@\"NSMutableData\""
- "@\"NSString\""
- "@\"NSString\"16@0:8"
- "@\"NSTimer\""
- "@\"NSURL\""
- "@\"NSURL\"16@0:8"
- "@\"NSURLSession\""
- "@\"NSURLSessionDataTask\""
- "@\"SubCalURLRequest\""
- "@16@0:8"
- "@24@0:8:16"
- "@24@0:8@16"
- "@28@0:8@16B24"
- "@32@0:8:16@24"
- "@32@0:8@16@24"
- "@32@0:8r*16Q24"
- "@40@0:8:16@24@32"
- "@40@0:8@16@24^@32"
- "@48@0:8@16@24^B32^@40"
- "B"
- "B16@0:8"
- "B24@0:8#16"
- "B24@0:8:16"
- "B24@0:8@\"Protocol\"16"
- "B24@0:8@16"
- "B32@0:8@16@24"
- "CDVURLWithPassword:"
- "CDVURLWithUser:"
- "ConsumerDictionarySupport"
- "DASubCalAccount"
- "DATask"
- "HTTPBody"
- "HTTPMethod"
- "NSObject"
- "NSURLSessionDataDelegate"
- "NSURLSessionDelegate"
- "NSURLSessionTaskDelegate"
- "Q"
- "Q16@0:8"
- "SubCalAccount"
- "SubCalDATask"
- "SubCalDATaskTrustDelegate"
- "SubCalDigest"
- "SubCalInsecureConnectionApproved"
- "SubCalLocalDBHelper"
- "SubCalSubscriptionURLKey"
- "SubCalTaskReachabilityError"
- "SubCalTitleKey"
- "SubCalURLRequest"
- "SubCalURLRequestDelegate"
- "SubCalUtilities"
- "SubCalValidationTask"
- "SubCalValidationTaskDelegate"
- "SubCalValidity"
- "T#,R"
- "T@\"<SubCalURLRequestDelegate>\",W,N,V_delegate"
- "T@\"<SubCalValidationTaskDelegate>\",W,N,V_delegate"
- "T@\"DACoreDAVTaskManager\",R,N"
- "T@\"DAStatusReport\",&,N,V_statusReport"
- "T@\"DATaskManager\",W,N,V_taskManager"
- "T@\"ICSDocument\",&,N,V_icsDocument"
- "T@\"NSData\",&,N,V_icsData"
- "T@\"NSData\",&,N,V_tmpICSData"
- "T@\"NSDate\",&,N,V_startTime"
- "T@\"NSDictionary\",&,N"
- "T@\"NSFileHandle\",&,N,V_fileHandle"
- "T@\"NSMutableData\",&,N,V_connectionData"
- "T@\"NSString\",&,N"
- "T@\"NSString\",&,N,V_calendarName"
- "T@\"NSString\",&,N,V_filePath"
- "T@\"NSString\",&,N,V_password"
- "T@\"NSString\",&,N,V_startRunloopDescriptionString"
- "T@\"NSString\",&,N,V_username"
- "T@\"NSString\",?,R,C"
- "T@\"NSString\",C,N,V_password"
- "T@\"NSString\",C,N,V_username"
- "T@\"NSString\",R,C"
- "T@\"NSString\",R,N"
- "T@\"NSTimer\",&,N,V_idleTimer"
- "T@\"NSURL\",&,N,V_subscriptionURL"
- "T@\"NSURL\",C,N,V_url"
- "T@\"NSURL\",R,N"
- "T@\"NSURLSession\",&,N,V_session"
- "T@\"NSURLSessionDataTask\",&,N,V_task"
- "T@\"SubCalURLRequest\",&,N,V_request"
- "TB,N"
- "TB,N,V_finished"
- "TB,N,V_foundBeginVCal"
- "TB,N,V_foundCalName"
- "TB,N,V_isManagedCalendar"
- "TB,N,V_performQuickValidation"
- "TB,N,V_sendDataUpdateCallback"
- "TB,N,V_useFileCache"
- "TB,N,V_useShortTimeout"
- "TB,N,V_useShortTimeoutInterval"
- "TB,N,V_wasUserRequested"
- "TB,R,N"
- "TQ,N,V_searchIndex"
- "TQ,R"
- "Td,N"
- "Td,N,V_timestamp"
- "Ti,N,V_subCalAccountVersion"
- "Tq,R,N,V_expectedDataSize"
- "Tq,R,N,V_receivedDataSize"
- "URL"
- "URLSession:dataTask:didBecomeDownloadTask:"
- "URLSession:dataTask:didBecomeStreamTask:"
- "URLSession:dataTask:didReceiveData:"
- "URLSession:dataTask:didReceiveResponse:completionHandler:"
- "URLSession:dataTask:willCacheResponse:completionHandler:"
- "URLSession:didBecomeInvalidWithError:"
- "URLSession:didCreateTask:"
- "URLSession:didReceiveChallenge:completionHandler:"
- "URLSession:task:didCompleteWithError:"
- "URLSession:task:didFinishCollectingMetrics:"
- "URLSession:task:didReceiveChallenge:completionHandler:"
- "URLSession:task:didReceiveInformationalResponse:"
- "URLSession:task:didSendBodyData:totalBytesSent:totalBytesExpectedToSend:"
- "URLSession:task:needNewBodyStream:"
- "URLSession:task:needNewBodyStreamFromOffset:completionHandler:"
- "URLSession:task:willBeginDelayedRequest:completionHandler:"
- "URLSession:task:willPerformHTTPRedirection:newRequest:completionHandler:"
- "URLSession:taskIsWaitingForConnectivity:"
- "URLSessionDidFinishEventsForBackgroundURLSession:"
- "URLWithString:"
- "Vv16@0:8"
- "^{_NSZone=}16@0:8"
- "_cachedICSFilesDirectory"
- "_calendarName"
- "_canAuthenticateAgainstProtectionSpace:"
- "_cancelIdleTimer"
- "_checkValidityWithConsumer:quickValidate:"
- "_connectionData"
- "_createIdleTimer"
- "_delegate"
- "_existingCalendarInCalDAVSourceWithExternalID:inSource:"
- "_expectedDataSize"
- "_extendIdleTimer"
- "_fileHandle"
- "_filePath"
- "_finishWithError:"
- "_finished"
- "_foundBeginVCal"
- "_foundCalName"
- "_handleAuthenticationChallenge:completionHandler:"
- "_icsData"
- "_icsDocument"
- "_idleTimer"
- "_idleTimerFired"
- "_initializeFileCache"
- "_isInvalidVCalBeginningForData:"
- "_isManagedCalendar"
- "_makeCalendarWithExternalId:inStore:error:"
- "_markEndTime"
- "_markStartTime"
- "_openFileHandle"
- "_password"
- "_performQuickValidation"
- "_receivedDataForFile:"
- "_receivedDataSize"
- "_relativePathFromCalDAVExternalID:"
- "_request"
- "_respondToChallenge:withCredential:noCredentialBehavior:completionHandler:"
- "_searchForCalNameInConnectionData:"
- "_searchIndex"
- "_sendDataUpdateCallback"
- "_session"
- "_setHeadersOnRequest:"
- "_setNonAppInitiated:"
- "_startRunloopDescriptionString"
- "_startTime"
- "_statusReport"
- "_stringBeforeNewline:length:"
- "_subCalAccountVersion"
- "_subscriptionURL"
- "_task"
- "_taskManager"
- "_timestamp"
- "_tmpICSCalendarPath"
- "_tmpICSData"
- "_tryQuickValidationCurrentData:"
- "_updateConstraintsIfNecessaryForSource:"
- "_url"
- "_useFileCache"
- "_useShortTimeout"
- "_useShortTimeoutInterval"
- "_username"
- "_wasUserRequested"
- "absoluteString"
- "account"
- "account:isValid:validationError:"
- "accountBoolPropertyForKey:"
- "accountDescription"
- "accountHasSignificantPropertyChangesWithChangeInfo:"
- "accountID"
- "accountIntPropertyForKey:"
- "accountPropertyForKey:"
- "accountType"
- "addEntriesFromDictionary:"
- "addObject:"
- "alarms"
- "allHTTPHeaderFields"
- "allKeys"
- "allowInsecureConnection"
- "appendData:"
- "arrayWithObjects:count:"
- "attachments"
- "authenticationMethod"
- "autorelease"
- "backingAccountInfo"
- "boolValue"
- "bundleForClass:"
- "bytes"
- "calDAVURLPath"
- "calendar"
- "calendarExternalId"
- "calendarForEntityType:eventStore:"
- "calendarName"
- "calendarWithExternalIdentifier:"
- "calendarsForEntityType:"
- "cancel"
- "cancelTaskWithReason:underlyingError:"
- "caseInsensitiveCompare:"
- "changeTrackingID"
- "class"
- "clearTmpICSData"
- "closeFile"
- "code"
- "commit:"
- "conformsToProtocol:"
- "connectionData"
- "constraintsName"
- "consumerDictKey"
- "consumerForTask:"
- "containsString:"
- "contentsOfDirectoryAtPath:error:"
- "cookiesEnabled"
- "count"
- "countByEnumeratingWithState:objects:count:"
- "createDirectoryAtPath:withIntermediateDirectories:attributes:error:"
- "credentialWithUser:password:persistence:"
- "currentAccountVersion"
- "currentHandler"
- "currentMode"
- "currentRunLoop"
- "d"
- "d16@0:8"
- "da_appendSlashIfNeeded"
- "da_hexString"
- "da_stringByAddingPercentEscapesForUsername"
- "da_urlByRemovingUsername"
- "da_urlBySettingPassword:"
- "da_urlBySettingUsername:"
- "dataTaskWithRequest:"
- "dataWithBytes:length:"
- "dataWithContentsOfMappedFile:"
- "date"
- "dateWithTimeIntervalSinceNow:"
- "debugDescription"
- "defaultManager"
- "defaultSessionConfiguration"
- "delegate"
- "description"
- "dictionaryWithExternalRepresentationData:"
- "dictionaryWithObjects:forKeys:count:"
- "didFinish"
- "digest"
- "discoverInitialPropertiesWithConsumer:"
- "domain"
- "doubleValue"
- "errorWithDomain:code:userInfo:"
- "eventStore"
- "eventStoreWithClientId:"
- "eventsMatchingPredicate:"
- "expectedDataSize"
- "externalID"
- "externalRepresentation"
- "externalRepresentationDataWithDictionary:"
- "fileExistsAtPath:"
- "fileHandle"
- "filePath"
- "fileSystemRepresentation"
- "finishTasksAndInvalidate"
- "finishWithError:"
- "finished"
- "foundBeginVCal"
- "foundCalName"
- "getCharacters:"
- "getSubscribedCalendarsSourceCreateIfNeededWithError:"
- "handleFailureInMethod:object:file:lineNumber:description:"
- "handleTrustChallenge:"
- "handleTrustChallenge:completionHandler:"
- "handleTrustChallenge:forSubCalURLRequest:"
- "handleTrustChallenge:forSubCalURLRequest:completionHandler:"
- "handleTrustChallenge:forTask:"
- "handleTrustChallenge:forTask:completionHandler:"
- "hasPrefix:"
- "hasSubscribedCalendarAtURL:"
- "hash"
- "host"
- "i16@0:8"
- "icsData"
- "icsDocument"
- "identifier"
- "idleTimer"
- "init"
- "initWithBackingAccountInfo:"
- "initWithBytes:length:encoding:"
- "initWithCapacity:"
- "initWithCustomClientId:"
- "initWithData:options:error:"
- "initWithEKOptions:path:changeTrackingClientId:enablePropertyModificationLogging:allowDelegateSources:"
- "initWithFileDescriptor:closeOnDealloc:"
- "initWithFireDate:interval:target:selector:userInfo:repeats:"
- "initWithObjectsAndKeys:"
- "initWithString:"
- "initWithURL:"
- "initWithURL:cachePolicy:timeoutInterval:"
- "initWithURL:wasUserRequested:"
- "initWithUTF8String:"
- "initializeCalendarWithExternalId:inSource:needsSave:error:"
- "initializeSourceWithExternalId:inStore:needsSave:error:"
- "invalidate"
- "invalidateAndCancel"
- "isChinaHolidayCalendar"
- "isDefaultAlarm"
- "isEqual:"
- "isEqualToAccount:"
- "isEqualToString:"
- "isFileURL"
- "isHolidaySubscribedCalendar"
- "isKindOfClass:"
- "isManagedCalendar"
- "isMemberOfClass:"
- "isProxy"
- "isSubCalAuthError"
- "isSubCalReachabilityError"
- "isSubCalURLString"
- "isSubscribedCalendarAccount"
- "isSyncedHolidayCalendar"
- "lastPathComponent"
- "length"
- "localizedIdenticalAccountFailureMessage"
- "localizedInvalidPasswordMessage"
- "localizedStringForKey:value:table:"
- "longLongValue"
- "lowercaseString"
- "modTagForSubCal"
- "mutableCopy"
- "newlineCharacterSet"
- "noteFailedNetworkRequest"
- "noteFailedProtocolRequest"
- "noteSuccessfulRequestWithNumDownloadedElements:"
- "noteTimeSpentInNetworking:"
- "numberWithBool:"
- "numberWithDouble:"
- "objectAtIndexedSubscript:"
- "objectForKeyedSubscript:"
- "oldAccountProperties"
- "onBehalfOfBundleIdentifier"
- "parentAccount"
- "parentAccountIdentifier"
- "password"
- "path"
- "performDelegateCallbackWithError:"
- "performQuickValidation"
- "performSelector:"
- "performSelector:withObject:"
- "performSelector:withObject:withObject:"
- "performTask"
- "port"
- "predicateForEventsInSubscribedCalendar:"
- "principalPath"
- "proposedCredential"
- "protectionSpace"
- "publicDescription"
- "q"
- "q16@0:8"
- "quickValidate:"
- "rangeOfString:"
- "rangeOfString:options:"
- "receivedDataSize"
- "refreshAllCalendars:"
- "refreshInterval"
- "registerWithiCalendar"
- "release"
- "removeAccountPropertyForKey:"
- "removeAlarm:"
- "removeAttachment:"
- "removeConsumerForTask:"
- "removeDBSyncDataForAccountChange:"
- "removeDataFromCalendar:forAccountChange:"
- "removeItemAtPath:error:"
- "request"
- "requestCancelTaskWithReason:"
- "resourceSpecifier"
- "respondsToSelector:"
- "resume"
- "retain"
- "retainCount"
- "rollback"
- "saveCalendar:commit:error:"
- "saveEvent:span:commit:error:"
- "saveTmpICSData"
- "scheme"
- "searchIndex"
- "self"
- "sendDataUpdateCallback"
- "session"
- "sessionWithConfiguration:delegate:delegateQueue:"
- "setAccount:"
- "setAccountBoolProperty:forKey:"
- "setAccountDescription:"
- "setAccountIntProperty:forKey:"
- "setAccountProperty:forKey:"
- "setAllHTTPHeaderFields:"
- "setAllowInsecureConnection:"
- "setAllowedEntityTypes:"
- "setCalDAVURLPath:"
- "setCalendarName:"
- "setConnectionData:"
- "setConstraintsName:"
- "setConsumer:forTask:"
- "setCurrentAccountVersion:"
- "setDelegate:"
- "setDigest:"
- "setDiscretionary:"
- "setExternalID:"
- "setExternalModificationTag:"
- "setExternalRepresentation:"
- "setFileHandle:"
- "setFilePath:"
- "setFinished:"
- "setFireDate:"
- "setFoundBeginVCal:"
- "setFoundCalName:"
- "setHTTPBody:"
- "setHTTPMethod:"
- "setHTTPShouldHandleCookies:"
- "setHost:"
- "setIcsData:"
- "setIcsDocument:"
- "setIdleTimer:"
- "setIsManagedCalendar:"
- "setObject:forKeyedSubscript:"
- "setPassword:"
- "setPerformQuickValidation:"
- "setReadOnly:"
- "setRefreshInterval:"
- "setRequest:"
- "setSearchIndex:"
- "setSendDataUpdateCallback:"
- "setSession:"
- "setShouldRemoveAlarms:"
- "setShouldRemoveAttachments:"
- "setSkipModificationValidation:"
- "setSource:"
- "setStartRunloopDescriptionString:"
- "setStartTime:"
- "setStatusReport:"
- "setSubCalAccountVersion:"
- "setSubscribed:"
- "setSubscribedCalendarRefreshFlags:inDictionary:"
- "setSubscriptionURL:"
- "setSyncId:"
- "setTask:"
- "setTaskManager:"
- "setTimeoutIntervalForRequest:"
- "setTimestamp:"
- "setTmpICSData:"
- "setURL:"
- "setURLCache:"
- "setUrl:"
- "setUseFTP:"
- "setUseFileCache:"
- "setUseSSL:"
- "setUseShortTimeout:"
- "setUseShortTimeoutInterval:"
- "setUsername:"
- "setValue:forHTTPHeaderField:"
- "setValue:forKey:"
- "setVersionForNewAccount"
- "setWasUserRequested:"
- "set_sourceApplicationBundleIdentifier:"
- "sharedLogger"
- "shouldForceNetworking"
- "shouldHoldPowerAssertion"
- "shouldRemoveAlarms"
- "shouldRemoveAttachments"
- "sourceType"
- "sourceWithExternalID:"
- "startConnection"
- "startModal"
- "startRunloopDescriptionString"
- "startTime"
- "statusCode"
- "statusReport"
- "stringByAppendingPathComponent:"
- "stringByAppendingString:"
- "stringByTrimmingCharactersInSet:"
- "stringWithFormat:"
- "subCalAccountVersion"
- "subCalTask:needsUsernameAndPasswordForHost:continuation:"
- "subCalURLRequest:didRedirectToURL:"
- "subCalURLRequest:finishedWithData:error:"
- "subCalURLRequest:updatedData:"
- "subCalURLRequestNeedsUsernameAndPasswordForHost:continuation:"
- "subCalValidationTask:downloadProgressedTo:outOf:"
- "subCalValidationTask:finishedWithError:calendarName:document:calendarData:"
- "subcalAccountID"
- "submitQueuedTask:"
- "subscribedCalendarRefreshFlagsFromDictionary:"
- "subscriptionURL"
- "substringFromIndex:"
- "superclass"
- "syncId"
- "task"
- "taskDidFinish:"
- "taskManager"
- "timeIntervalSinceDate:"
- "timeIntervalSinceNow"
- "timestamp"
- "tmpICSData"
- "upgradeAccount"
- "upgradeAccountSpecificPropertiesOnAccount:inStore:parentAccount:"
- "url"
- "useFTP"
- "useFileCache"
- "useSSL"
- "useShortTimeout"
- "useShortTimeoutInterval"
- "user"
- "userInfo"
- "username"
- "v16@0:8"
- "v20@0:8B16"
- "v20@0:8i16"
- "v24@0:8@\"DATaskManager\"16"
- "v24@0:8@\"NSError\"16"
- "v24@0:8@\"NSURLSession\"16"
- "v24@0:8@16"
- "v24@0:8Q16"
- "v24@0:8d16"
- "v28@0:8@16B24"
- "v28@0:8i16@\"NSError\"20"
- "v28@0:8i16@20"
- "v32@0:8@\"NSString\"16@?<v@?@\"NSString\"@\"NSString\">24"
- "v32@0:8@\"NSURLAuthenticationChallenge\"16@\"SubCalDATask\"24"
- "v32@0:8@\"NSURLAuthenticationChallenge\"16@\"SubCalURLRequest\"24"
- "v32@0:8@\"NSURLSession\"16@\"NSError\"24"
- "v32@0:8@\"NSURLSession\"16@\"NSURLSessionTask\"24"
- "v32@0:8@\"SubCalURLRequest\"16@\"NSData\"24"
- "v32@0:8@\"SubCalURLRequest\"16@\"NSURL\"24"
- "v32@0:8@16@24"
- "v32@0:8@16@?24"
- "v40@0:8@\"NSURLAuthenticationChallenge\"16@\"SubCalDATask\"24@?<v@?q@\"NSURLCredential\">32"
- "v40@0:8@\"NSURLAuthenticationChallenge\"16@\"SubCalURLRequest\"24@?<v@?q@\"NSURLCredential\">32"
- "v40@0:8@\"NSURLSession\"16@\"NSURLAuthenticationChallenge\"24@?<v@?q@\"NSURLCredential\">32"
- "v40@0:8@\"NSURLSession\"16@\"NSURLSessionDataTask\"24@\"NSData\"32"
- "v40@0:8@\"NSURLSession\"16@\"NSURLSessionDataTask\"24@\"NSURLSessionDownloadTask\"32"
- "v40@0:8@\"NSURLSession\"16@\"NSURLSessionDataTask\"24@\"NSURLSessionStreamTask\"32"
- "v40@0:8@\"NSURLSession\"16@\"NSURLSessionTask\"24@\"NSError\"32"
- "v40@0:8@\"NSURLSession\"16@\"NSURLSessionTask\"24@\"NSHTTPURLResponse\"32"
- "v40@0:8@\"NSURLSession\"16@\"NSURLSessionTask\"24@\"NSURLSessionTaskMetrics\"32"
- "v40@0:8@\"NSURLSession\"16@\"NSURLSessionTask\"24@?<v@?@\"NSInputStream\">32"
- "v40@0:8@\"SubCalURLRequest\"16@\"NSData\"24@\"NSError\"32"
- "v40@0:8@\"SubCalValidationTask\"16q24q32"
- "v40@0:8@16@24@32"
- "v40@0:8@16@24@?32"
- "v40@0:8@16q24q32"
- "v44@0:8@16@24i32@?36"
- "v48@0:8@\"NSURLSession\"16@\"NSURLSessionDataTask\"24@\"NSCachedURLResponse\"32@?<v@?@\"NSCachedURLResponse\">40"
- "v48@0:8@\"NSURLSession\"16@\"NSURLSessionDataTask\"24@\"NSURLResponse\"32@?<v@?q>40"
- "v48@0:8@\"NSURLSession\"16@\"NSURLSessionTask\"24@\"NSURLAuthenticationChallenge\"32@?<v@?q@\"NSURLCredential\">40"
- "v48@0:8@\"NSURLSession\"16@\"NSURLSessionTask\"24@\"NSURLRequest\"32@?<v@?q@\"NSURLRequest\">40"
- "v48@0:8@\"NSURLSession\"16@\"NSURLSessionTask\"24q32@?<v@?@\"NSInputStream\">40"
- "v48@0:8@16@24@32@?40"
- "v48@0:8@16@24q32@?40"
- "v56@0:8@\"NSURLSession\"16@\"NSURLSessionTask\"24@\"NSHTTPURLResponse\"32@\"NSURLRequest\"40@?<v@?@\"NSURLRequest\">48"
- "v56@0:8@\"NSURLSession\"16@\"NSURLSessionTask\"24q32q40q48"
- "v56@0:8@\"SubCalValidationTask\"16@\"NSError\"24@\"NSString\"32@\"ICSDocument\"40@\"NSData\"48"
- "v56@0:8@16@24@32@40@48"
- "v56@0:8@16@24@32@40@?48"
- "v56@0:8@16@24q32q40q48"
- "valueForHTTPHeaderField:"
- "wasUserInitiated"
- "wasUserRequested"
- "willFinish"
- "writeData:"
- "writeToFile:atomically:"
- "x_wr_caldesc"
- "x_wr_calname"
- "zone"

```
