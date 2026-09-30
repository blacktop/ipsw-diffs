## IntelligenceFlowPlannerSupport

> `FileSystem/System/Library/PrivateFrameworks/IntelligenceFlowPlannerSupport.framework/PlannerModelFacingErrors.loctable`

```diff

 en.plannerTool.error.propertyNotFound = "Property ‘%1$@’ not found in entity ‘%2$@’"
 en.plannerTool.error.searchInApp.notSupported = "The app '%@' does not support in-app search."
 en.plannerTool.error.unexpectedArgumentKeys = "Unexpected argument keys. Expected keys: [%1$@], got: [%2$@]. Each parameter must be a separate JSON key."
-en.plannerTool.globalSearch.missingSupportInSouthKorea = "Search is not supported in South Korea. Do not invoke find or make any further web or search queries for this request."
+en.plannerTool.globalSearch.missingSupportInSouthKorea = "Maps search is not supported in South Korea. Do not invoke find for maps search for this request."
 en.plannerTool.globalSearch.wkaSafetyActionDecline = "CONTENT RESTRICTION: This result is subject to a legal content restriction and must not be summarized, paraphrased, or answered. Do not generate any response about this topic from your own knowledge. You must immediately decline this request to the user."
 en.plannerTool.home.invalidUnit = "Invalid unit"
 en.plannerTool.home.missingValue = "missing value"

 en.plannerTool.makeDatetime.unresolvedTimezone = "Could not resolve \"%@\" to a timezone. Pass an IANA identifier (e.g. \"Europe/Rome\", \"America/Los_Angeles\", \"Asia/Tokyo\"), or call `find` to look up the IANA identifier for this place and retry."
 en.plannerTool.makeDatetime.unsupportedUnit = "Unsupported unit '%@'. Expected weekday name, 'weekend', 'weekday', 'week', 'day', 'month', or 'year'."
 en.plannerTool.makeDatetime.weekScopeNotSupportedForWeekdayQueries = "Week scope is not supported for weekday queries."
+en.plannerTool.maps.addressNotUniquelyResolved = "Couldn't resolve the %1$@ address to a single place. Pass MapsPlaceEntity or the specific address as a string in `%2$@` instead."
 en.plannerTool.maps.calendarEventHasNoLocation = "This calendar event doesn't have an address. Try searching for the location by name instead."
 en.plannerTool.maps.cantDecodeDestinationIdOnSimulator = "Cannot decode destination_id on simulator"
 en.plannerTool.maps.contactHasMultipleAddresses = "ContactEntity has multiple postal addresses. Pass the specific address as a string in `to_locations` instead"
 en.plannerTool.maps.contactHasNoAddress = "This contact doesn't have an address"
+en.plannerTool.maps.contactRelationshipNeedsFind = "\"%1$@\" is a contact name, not a place. Call `find` to look up the contact, then pass the requested contact's postal address as a string in `%2$@`."
 en.plannerTool.maps.couldNotResolveDestinationAddressOrName = "Could not resolve destination address or name."
 en.plannerTool.maps.couldNotResolveOriginAddressOrName = "Could not resolve origin address or name."
 en.plannerTool.maps.destinationEntityMissingPlaceProperty = "Destination entity missing place property."

 en.plannerTool.play.unsupportedEntityDomain = "Unsupported entity domain: %@"
 en.plannerTool.reminders.eitherReminderIdsOrListIdsRequired = "Either ‘reminder_ids’ or ‘list_ids’ must be provided"
 en.plannerTool.reminders.updateRequiresAtLeastOneField = "At least one field to update must be provided"
+en.plannerTool.search.drivingPhotoRestriction = "CARPLAY RESTRICTION: Photos can't be shown while connected to CarPlay. Do not display or describe the results; tell the user you can't show photos while they're in the car."
 en.plannerTool.search.unsupportedEntitySource = "Unsupported entity source found: %@. Only ‘local’, ‘global’, and ‘answerSynthesis’ sources are supported."
 en.plannerTool.search.urlBasedSearchesNotSupportedInSafari = "URL-based searches are not supported in Safari"
 en.plannerTool.shared.contactForDestination_ids = "We do not support sending intercom messages to people. Only home, rooms, and zones are allowed"

```
