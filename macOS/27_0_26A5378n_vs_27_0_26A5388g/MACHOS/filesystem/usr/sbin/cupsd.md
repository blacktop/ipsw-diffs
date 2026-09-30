## cupsd

> `/usr/sbin/cupsd`

### Sections with Same Size but Changed Content

- `__DATA_CONST.__const`
- `__DATA_CONST.__cfstring`
- `__DATA_CONST.__got`
- `__DATA_CONST.__auth_ptr`

```diff

-530.0.0.0.0
-  __TEXT.__text: 0x4358c
-  __TEXT.__auth_stubs: 0x1f30
-  __TEXT.__cstring: 0x118a1
-  __TEXT.__const: 0x348
+531.1.0.0.0
+  __TEXT.__text: 0x3fa0c
+  __TEXT.__auth_stubs: 0x1f20
+  __TEXT.__cstring: 0x10c29
+  __TEXT.__const: 0x340
   __TEXT.__oslogstring: 0x6b
-  __TEXT.__unwind_info: 0x588
+  __TEXT.__unwind_info: 0x540
   __DATA_CONST.__const: 0xda8
   __DATA_CONST.__cfstring: 0xc0
-  __DATA_CONST.__auth_got: 0xf98
+  __DATA_CONST.__auth_got: 0xf90
   __DATA_CONST.__got: 0x120
   __DATA_CONST.__auth_ptr: 0x78
-  __DATA.__data: 0x224
+  __DATA.__data: 0x21c
   __DATA.__bss: 0x891
-  __DATA.__common: 0x4a0
+  __DATA.__common: 0x490
   - /System/Library/Frameworks/ApplicationServices.framework/Versions/A/ApplicationServices
   - /System/Library/Frameworks/ColorSync.framework/Versions/A/ColorSync
   - /System/Library/Frameworks/CoreFoundation.framework/Versions/A/CoreFoundation

   - /usr/lib/libpam.2.dylib
   - /usr/lib/libresolv.9.dylib
   - /usr/lib/libz.1.dylib
-  Functions: 412
-  Symbols:   533
-  CStrings:  2713
+  Functions: 392
+  Symbols:   532
+  CStrings:  2610
 
Symbols:
- _ippWriteFile
CStrings:
+ "%s: %s %s"
+ "%s: %s (dest=%s job=%d) %s"
+ "%s: %s (dest=%s) %s"
+ "%s: Rejecting a proxy URI: hostname=%s."
+ "%s: device_uri is missing."
+ "%s: httpSeparateURI err:%d. uri=%s"
+ "Printer name is missing."
+ "The printer is in use."
+ "cupsdAddEvent"
+ "cupsdReadClient"
- "# Subscription configuration file for CUPS v2.3.4\n"
- "%s/notifier/%s"
- "%s/subscriptions.conf"
- "."
- ".."
- "<%02X"
- "</Subscription>"
- "</Subscription>\n"
- "<Subscription"
- "<Subscription %d>\n"
- ">\n"
- ">%c"
- "Added subscription #%d for job %d."
- "Added subscription #%d for printer \"%s\"."
- "Added subscription #%d for server."
- "Added subscription %d for job %d"
- "Bad UserData '%s' on line %d of subscriptions.conf."
- "Bad notify-pull-method \"%s\"."
- "Bad notify-recipient-uri \"%s\"."
- "Bad notify-user-data \"%s\"."
- "Character set \"%s\" not supported."
- "Discarding unused %s event..."
- "Events"
- "Events %s\n"
- "ExpirationTime"
- "ExpirationTime %ld\n"
- "Expiring subscriptions..."
- "Interval"
- "Interval %d\n"
- "Job %s not found on line %d of subscriptions.conf."
- "Job subscriptions cannot be renewed."
- "JobId"
- "JobId %d\n"
- "Language \"%s\" not supported."
- "LeaseDuration"
- "LeaseDuration %d\n"
- "Missing notify-subscription-ids attribute."
- "NextEventId"
- "NextEventId %d\n"
- "NextSubscriptionId"
- "NextSubscriptionId %d\n"
- "No subscription attributes in request."
- "No subscriptions found."
- "Notifier %s started - PID = %d"
- "Notifier for subscription %d (%s) went away, retrying!"
- "Owner"
- "Owner %s\n"
- "Printer '%s' not found on line %d of subscriptions.conf."
- "PrinterName"
- "PrinterName %s\n"
- "Recipient"
- "Recipient %s\n"
- "Saving subscriptions.conf..."
- "Subscription #%d does not exist."
- "Subscription %d has expired..."
- "Syntax error on line %d of subscriptions.conf."
- "The notify-lease-duration attribute cannot be used with job subscriptions."
- "The notify-user-data value is too large (%d > 63 octets)."
- "There are too many subscriptions."
- "Unable to allocate memory for event - %s"
- "Unable to allocate memory for subscription #%d!"
- "Unable to allocate memory for subscription object - %s"
- "Unable to allocate memory for subscriptions - %s"
- "Unable to create pipes for notifier %s - %s"
- "Unable to create pipes for notifier status - %s"
- "Unable to fork for notifier %s - %s"
- "Unable to send event for subscription %d (%s)!"
- "Unknown configuration directive %s on line %d of subscriptions.conf."
- "Unknown event name '%s' on line %d of subscriptions.conf."
- "UserData"
- "UserData "
- "[Notifier]"
- "cancel_subscription(con=%p[%d], sub_id=%d)"
- "copy_subscription_attrs(con=%p, sub=%p, ra=%p, exclude=%p)"
- "copy_subscription_attrs: notify-events"
- "create_subscriptions(con=%p(%d), uri=\"%s\")"
- "create_subscriptions: Limiting notify-lease-duration to %d seconds."
- "cupsdAddEvent(event=%s, dest=%p(%s), job=%p(%d), text=\"%s\", ...)"
- "cupsdAddEvent: Discarding %s event since MaxEvents is %d!"
- "cupsdAddSubscription(mask=%x, dest=%p(%s), job=%p(%d), uri=\"%s\")"
- "cupsdAddSubscription: Reached MaxSubscriptions %d (count=%d)"
- "cupsdAddSubscription: Reached MaxSubscriptionsPerJob %d for job #%d (count=%d)"
- "cupsdAddSubscription: Reached MaxSubscriptionsPerPrinter %d for %s (count=%d)"
- "cupsd_send_notification(sub=%p(%d), event=%p(%s))"
- "en-US"
- "get_notifications(con=%p[%d])"
- "get_subscription_attrs(con=%p[%d], sub_id=%d)"
- "get_subscriptions(con=%p[%d], uri=%s)"
- "mailto:"
- "my-subscriptions"
- "notify-charset"
- "notify-events not specified."
- "notify-get-interval"
- "notify-job-id"
- "notify-lease-duration=%d"
- "notify-natural-language"
- "notify-printer-uri"
- "notify-recipient-uri URI \"%s\" is already used."
- "notify-recipient-uri URI \"%s\" uses unknown scheme."
- "notify-sequence-number"
- "notify-sequence-numbers"
- "notify-status-code"
- "notify-subscribed-event"
- "notify-subscription-ids"
- "notify-text"
- "notify-time-interval"
- "notify-time-interval=%d"
- "pullmethod=\"%s\""
- "recipient=\"%s\""
- "renew_subscription(con=%p[%d], sub_id=%d)"
- "renew_subscription: Limiting notify-lease-duration to %d seconds."
- "rss:"
- "sub->pipe=%d"
```
