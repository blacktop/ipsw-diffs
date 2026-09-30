## CalendarFoundation

> `/System/Library/PrivateFrameworks/CalendarFoundation.framework/Versions/A/CalendarFoundation`

```diff

-1575.3.2.0.0
-  __TEXT.__text: 0x629d8
-  __TEXT.__auth_stubs: 0xf80
-  __TEXT.__objc_methlist: 0x5750
-  __TEXT.__cstring: 0x6ef2
-  __TEXT.__const: 0x3b4
+1575.5.3.0.0
+  __TEXT.__text: 0x63060
+  __TEXT.__auth_stubs: 0xf70
+  __TEXT.__objc_methlist: 0x5d1c
+  __TEXT.__cstring: 0x6ee2
+  __TEXT.__const: 0x3a4
   __TEXT.__gcc_except_tab: 0xa90
   __TEXT.__oslogstring: 0x35d5
   __TEXT.__ustring: 0xf0

   __TEXT.__swift5_fieldmd: 0x50
   __TEXT.__swift5_proto: 0xc
   __TEXT.__swift5_types: 0x8
-  __TEXT.__unwind_info: 0x19b8
-  __TEXT.__objc_classname: 0xbbe
-  __TEXT.__objc_methname: 0xedae
-  __TEXT.__objc_methtype: 0x1813
-  __TEXT.__objc_stubs: 0xacc0
-  __DATA_CONST.__got: 0x760
+  __TEXT.__unwind_info: 0x1a60
+  __TEXT.__objc_classname: 0xbd4
+  __TEXT.__objc_methname: 0xeeb7
+  __TEXT.__objc_methtype: 0x1823
+  __TEXT.__objc_stubs: 0xadc0
+  __DATA_CONST.__got: 0x768
   __DATA_CONST.__const: 0xd88
-  __DATA_CONST.__objc_classlist: 0x348
+  __DATA_CONST.__objc_classlist: 0x350
   __DATA_CONST.__objc_catlist: 0xb0
   __DATA_CONST.__objc_protolist: 0xa8
   __DATA_CONST.__objc_imageinfo: 0x8
-  __DATA_CONST.__objc_selrefs: 0x40c8
+  __DATA_CONST.__objc_selrefs: 0x4240
   __DATA_CONST.__objc_protorefs: 0x8
-  __DATA_CONST.__objc_superrefs: 0x188
+  __DATA_CONST.__objc_superrefs: 0x190
   __DATA_CONST.__objc_arraydata: 0xf8
-  __AUTH_CONST.__auth_got: 0x7d0
+  __AUTH_CONST.__auth_got: 0x7c8
   __AUTH_CONST.__const: 0x1788
-  __AUTH_CONST.__cfstring: 0x9600
-  __AUTH_CONST.__objc_const: 0x8040
+  __AUTH_CONST.__cfstring: 0x95e0
+  __AUTH_CONST.__objc_const: 0x7848
   __AUTH_CONST.__objc_arrayobj: 0x78
   __AUTH_CONST.__objc_intobj: 0x18
-  __AUTH.__objc_data: 0xaa0
+  __AUTH.__objc_data: 0xaf0
   __AUTH.__data: 0x98
-  __DATA.__objc_ivar: 0x34c
+  __DATA.__objc_ivar: 0x354
   __DATA.__data: 0x9f8
   __DATA.__bss: 0x800
   __DATA_DIRTY.__objc_data: 0x15e0

   - /usr/lib/swift/libswiftos.dylib
   - /usr/lib/swift/libswiftsys_time.dylib
   - /usr/lib/swift/libswiftunistd.dylib
-  UUID: D4C9E7F6-C2BC-3986-9B99-A120BE5805CD
-  Functions: 2505
-  Symbols:   6213
-  CStrings:  5684
+  UUID: 3A4A0507-6E3F-31B6-8F14-446B725D0294
+  Functions: 2588
+  Symbols:   6318
+  CStrings:  5695
 
Symbols:
+ +[CalAccountUtils _accountStore].cold.1
+ +[CalAppleConferenceFormat _conferenceTitleRegex].cold.1
+ +[CalAppleConferenceFormat _detailsDelimiterRegex].cold.1
+ +[CalAppleConferenceFormat _joinMethodTitleAndFeaturesRegex].cold.1
+ +[CalAppleConferenceFormat _startDelimiterRegex].cold.1
+ +[CalAppleConferenceFormat calConferenceSerializationHandle].cold.1
+ +[CalCFPreferencesStore shared].cold.1
+ +[CalCalendarConstraints backwardsCompatibleConstraintsPathForName:].cold.1
+ +[CalConferencePersistence _knownPersistenceFormats].cold.1
+ +[CalConferenceURLDetector _googleMeetSuffix].cold.1
+ +[CalConferenceURLDetector _hasDisallowedPathExtension:].cold.1
+ +[CalConferenceURLDetector _microsoftSafeLinkPrefix].cold.1
+ +[CalConferenceUtilities conferenceURLHasAllowedScheme:].cold.2
+ +[CalContactsProvider defaultProvider].cold.1
+ +[CalDistributedNotificationCenter defaultCenter].cold.1
+ +[CalEntitlementsVerifier currentProcessCanAccessProcedureOrEmailAlarms]
+ +[CalEntitlementsVerifier currentProcessIsShortcuts]
+ +[CalFloatingDateHelper dateInFloatingTimeZoneFromDate:inTimeZone:].cold.1
+ +[CalFloatingDateHelper dateInTimeZone:fromFloatingDateInGMT:].cold.1
+ +[CalFoundationLogSubsystem accounts].cold.1
+ +[CalFoundationLogSubsystem contacts].cold.1
+ +[CalFoundationLogSubsystem defaultCategory].cold.1
+ +[CalFoundationLogSubsystem eventTimer].cold.1
+ +[CalFoundationLogSubsystem junk].cold.1
+ +[CalFoundationLogSubsystem locations].cold.1
+ +[CalFoundationLogSubsystem memory].cold.1
+ +[CalFoundationLogSubsystem messageTrace].cold.1
+ +[CalFoundationLogSubsystem suggestions].cold.1
+ +[CalFoundationPreferences shared].cold.1
+ +[CalGoogleConferenceFormat _delimiterRegex].cold.1
+ +[CalGoogleConferenceFormat calConferenceSerializationHandle].cold.1
+ +[CalHolidayAccountUtils logHandle].cold.1
+ +[CalLocationAuthorization locationAuthorizationAsyncCallersQueue].cold.1
+ +[CalLocationAuthorization logHandle].cold.1
+ +[CalLocationManager _loadMapKit].cold.1
+ +[CalOpenFileURLWrapper supportsSecureCoding]
+ +[CalPersonaUtils personalPersonaIdentifier].cold.1
+ +[CalPreferences _debugColorPreferences].cold.1
+ +[CalPreferences log].cold.1
+ +[CalRecurrenceRuleDescriptionGenerator _daysOfWeek].cold.1
+ +[CalSpotlightPendingSearch _queue].cold.1
+ +[CalStructuredDataArchiver defaultPermittedClasses].cold.1
+ +[CalSubscribedCalendarExternalRepresentation logHandle].cold.1
+ +[CalSuggestionsProvider defaultProvider].cold.1
+ +[CalSystemInformation isRunningAsSetupUser].cold.1
+ +[CalSystemInformation systemBuildVersion].cold.1
+ +[CaliCalendarAnonymizer sharedAnonymizedDomainName].cold.1
+ +[CaliCalendarAnonymizer sharedAnonymizedStringsCount].cold.1
+ +[CaliCalendarAnonymizer sharedAnonymizedStrings].cold.1
+ +[EKCalendarDate initialize].cold.1
+ +[NSCalendar(CalClassAdditions) CalGregorianGMTCalendar].cold.1
+ +[NSCalendar(CalClassAdditions) CalYearlessDateThreshold].cold.1
+ +[NSDate(CalClassAdditions) calGMT].cold.1
+ +[NSString(CalClassAdditions) CalAutoCommentPrefix].cold.1
+ -[ACAccount(CalAdditions) _calDAVDataclassProperties].cold.1
+ -[CalAsyncBlockQueue initWithBlockPerformer:].cold.1
+ -[CalCancelableDispatchBlock initWithBlock:inQueue:].cold.1
+ -[CalCancelableDispatchBlock initWithBlock:inQueue:].cold.2
+ -[CalCancelablePerformSelector initWithBlock:].cold.1
+ -[CalCancelableRunLoopPerformBlock initWithBlock:inRunLoop:].cold.1
+ -[CalCancelableRunLoopPerformBlock initWithBlock:inRunLoop:].cold.2
+ -[CalDateRange briefDescription].cold.1
+ -[CalDateRange midnightsForRangeInTimeZoneString:].cold.1
+ -[CalDispatchQueueAsyncBlockPerformer initWithQueue:].cold.1
+ -[CalLocationAuthorization locationManagerDidChangeAuthorization:].cold.1
+ -[CalOpenFileURLWrapper .cxx_destruct]
+ -[CalOpenFileURLWrapper copyWithZone:]
+ -[CalOpenFileURLWrapper encodeWithCoder:]
+ -[CalOpenFileURLWrapper file]
+ -[CalOpenFileURLWrapper initWithCoder:]
+ -[CalOpenFileURLWrapper initWithURL:]
+ -[CalOpenFileURLWrapper isEqual:]
+ -[CalOpenFileURLWrapper url]
+ -[CalSpotlightPendingSearch searchWithString:].cold.1
+ -[CalStopwatch elapsedTimeInNanoseconds].cold.1
+ -[EKCalendarDate description].cold.1
+ -[NSDate(CalClassAdditions) _stringWithUseAbbreviatedFormats:lowerCase:].cold.1
+ -[NSString(CalClassAdditions) CalSafeFilename].cold.1
+ -[NSString(CalClassAdditions) stringByEncodingSlashes].cold.1
+ -[NSString(CalClassAdditions) stringByURLEscapingAllReservedCharacters].cold.1
+ -[NSString(CalClassAdditions) stringByURLQuoting].cold.1
+ CalAnalyticsTimeIntervalFromMachTimes.cold.1
+ CalRedactURLString.cold.1
+ CalendarFoundationPerformBlockOnSharedContactStore.cold.1
+ CurrentLocaleExpectsSurnameFirst.cold.1
+ EKCachedTimeZoneWithName.cold.1
+ EKSymbolicColorToRGBMapping.cold.1
+ GetStaticAutoUpdatingCurrentLocale.cold.1
+ OBJC_IVAR_$_CalOpenFileURLWrapper._file
+ OBJC_IVAR_$_CalOpenFileURLWrapper._url
+ _EKSharedGregorianCalendarLock.cold.1
+ _OBJC_CLASS_$_CalOpenFileURLWrapper
+ _OBJC_CLASS_$_NSFileHandle
+ _OBJC_METACLASS_$_CalOpenFileURLWrapper
+ __OBJC_$_CLASS_METHODS_CalOpenFileURLWrapper
+ __OBJC_$_CLASS_PROP_LIST_CalOpenFileURLWrapper
+ __OBJC_$_INSTANCE_METHODS_CalOpenFileURLWrapper
+ __OBJC_$_INSTANCE_VARIABLES_CalOpenFileURLWrapper
+ __OBJC_$_PROP_LIST_CalOpenFileURLWrapper
+ __OBJC_CLASS_PROTOCOLS_$_CalOpenFileURLWrapper
+ __OBJC_CLASS_RO_$_CalOpenFileURLWrapper
+ __OBJC_METACLASS_RO_$_CalOpenFileURLWrapper
+ _objc_msgSend$currentProcessHasSyncClientEntitlement
+ _objc_msgSend$currentProcessHasTestingEntitlement
+ _objc_msgSend$currentProcessIsAutomator
+ _objc_msgSend$currentProcessIsCalendarDaemon
+ _objc_msgSend$currentProcessIsShortcuts
+ _objc_msgSend$initWithFileDescriptor:closeOnDealloc:
+ _objc_msgSend$startAccessingSecurityScopedResource
+ _objc_msgSend$stopAccessingSecurityScopedResource
+ _phoneNumberDetector.cold.1
+ _startTimes.cold.1
- _OUTLINED_FUNCTION_8
- _OUTLINED_FUNCTION_9
- _strcmp
CStrings:
+ "%ld days after (%@)"
+ "%ld days before (%@)"
+ "1 week before"
+ "@\"NSFileHandle\""
+ "Alert %ld days after at %@"
+ "Alert %ld days before at %@"
+ "Alert 1 week before"
+ "CalOpenFileURLWrapper"
+ "T@\"NSFileHandle\",R,N,V_file"
+ "T@\"NSURL\",R,N,V_url"
+ "_file"
+ "_url"
+ "com.apple.shortcuts"
+ "currentProcessCanAccessProcedureOrEmailAlarms"
+ "currentProcessIsShortcuts"
+ "initWithFileDescriptor:closeOnDealloc:"
+ "initWithURL:"
+ "startAccessingSecurityScopedResource"
+ "stopAccessingSecurityScopedResource"
- "%d day before (%@)"
- "%d week before"
- "%ld %@ after (%@)"
- "%ld %@ before (%@)"
- "Alert %d day before at %@"
- "Alert %d week before"
- "Alert %ld %@ after at %@"
- "Alert %ld %@ before at %@"

```
