## apple-cloud-enhanced-security

> Group: ⬆️ Updated

```diff

 	(profile-flag "deny-lsopen")
 )
 
+(allow mach-bootstrap
+	(apply-message-filter
+		(allow mach-message-send
+			(message-number 804)
+		)
+		(allow mach-message-send
+			(require-all
+				(message-number 805)
+				(state-flag "blastdoor-post-launch")
+				(require-not (message-number 804))
+			)
+		)
+		(allow mach-message-send
+			(require-all
+				(message-number 805)
+				(message-number 802)
+				(require-not (message-number 804))
+				(require-not (state-flag "blastdoor-post-launch"))
+			)
+		)
+		(allow mach-message-send
+			(require-all
+				(message-number 805)
+				(message-number 805)
+				(require-not (message-number 804))
+				(require-not (state-flag "blastdoor-post-launch"))
+				(require-not (message-number 802))
+			)
+		)
+		(allow mach-message-send
+			(require-all
+				(message-number 805)
+				(message-number 904)
+				(require-not (message-number 804))
+				(require-not (state-flag "blastdoor-post-launch"))
+				(require-not (message-number 802))
+				(require-not (message-number 805))
+			)
+		)
+		(allow mach-message-send
+			(require-all
+				(message-number 803)
+				(require-not (message-number 804))
+				(require-not (message-number 805))
+			)
+		)
+		(allow mach-message-send
+			(require-all
+				(message-number 711)
+				(require-not (message-number 804))
+				(require-not (message-number 805))
+				(require-not (message-number 803))
+			)
+		)
+		(allow mach-message-send
+			(require-all
+				(message-number 904)
+				(state-flag "blastdoor-post-launch")
+				(require-not (message-number 804))
+				(require-not (message-number 805))
+				(require-not (message-number 803))
+				(require-not (message-number 711))
+			)
+		)
+		(allow mach-message-send
+			(require-all
+				(message-number 904)
+				(message-number 802)
+				(require-not (message-number 804))
+				(require-not (message-number 805))
+				(require-not (message-number 803))
+				(require-not (message-number 711))
+				(require-not (state-flag "blastdoor-post-launch"))
+			)
+		)
+		(allow mach-message-send
+			(require-all
+				(message-number 904)
+				(message-number 805)
+				(require-not (message-number 804))
+				(require-not (message-number 805))
+				(require-not (message-number 803))
+				(require-not (message-number 711))
+				(require-not (state-flag "blastdoor-post-launch"))
+				(require-not (message-number 802))
+			)
+		)
+		(allow mach-message-send
+			(require-all
+				(message-number 904)
+				(message-number 904)
+				(require-not (message-number 804))
+				(require-not (message-number 805))
+				(require-not (message-number 803))
+				(require-not (message-number 711))
+				(require-not (state-flag "blastdoor-post-launch"))
+				(require-not (message-number 802))
+				(require-not (message-number 805))
+			)
+		)
+		(allow mach-message-send
+			(require-all
+				(message-number 206)
+				(require-not (message-number 804))
+				(require-not (message-number 805))
+				(require-not (message-number 803))
+				(require-not (message-number 711))
+				(require-not (message-number 904))
+			)
+		)
+		(allow mach-message-send
+			(require-all
+				(message-number 800)
+				(require-not (message-number 804))
+				(require-not (message-number 805))
+				(require-not (message-number 803))
+				(require-not (message-number 711))
+				(require-not (message-number 904))
+				(require-not (message-number 206))
+			)
+		)
+		(allow mach-message-send
+			(require-all
+				(message-number 712)
+				(require-not (message-number 804))
+				(require-not (message-number 805))
+				(require-not (message-number 803))
+				(require-not (message-number 711))
+				(require-not (message-number 904))
+				(require-not (message-number 206))
+				(require-not (message-number 800))
+			)
+		)
+		(allow mach-message-send
+			(require-all
+				(message-number 207)
+				(require-not (message-number 804))
+				(require-not (message-number 805))
+				(require-not (message-number 803))
+				(require-not (message-number 711))
+				(require-not (message-number 904))
+				(require-not (message-number 206))
+				(require-not (message-number 800))
+				(require-not (message-number 712))
+			)
+		)
+		(allow mach-message-send
+			(require-all
+				(message-number 718)
+				(require-not (message-number 804))
+				(require-not (message-number 805))
+				(require-not (message-number 803))
+				(require-not (message-number 711))
+				(require-not (message-number 904))
+				(require-not (message-number 206))
+				(require-not (message-number 800))
+				(require-not (message-number 712))
+				(require-not (message-number 207))
+			)
+		)
+		(allow mach-message-send
+			(require-all
+				(message-number 802)
+				(require-not (message-number 804))
+				(require-not (message-number 805))
+				(require-not (message-number 803))
+				(require-not (message-number 711))
+				(require-not (message-number 904))
+				(require-not (message-number 206))
+				(require-not (message-number 800))
+				(require-not (message-number 712))
+				(require-not (message-number 207))
+				(require-not (message-number 718))
+				(require-not (state-flag "blastdoor-post-launch"))
+			)
+		)
+		(allow mach-message-send
+			(require-all
+				(message-number 805)
+				(require-not (message-number 804))
+				(require-not (message-number 805))
+				(require-not (message-number 803))
+				(require-not (message-number 711))
+				(require-not (message-number 904))
+				(require-not (message-number 206))
+				(require-not (message-number 800))
+				(require-not (message-number 712))
+				(require-not (message-number 207))
+				(require-not (message-number 718))
+				(require-not (state-flag "blastdoor-post-launch"))
+				(require-not (message-number 802))
+			)
+		)
+		(allow mach-message-send
+			(require-all
+				(message-number 904)
+				(require-not (message-number 804))
+				(require-not (message-number 805))
+				(require-not (message-number 803))
+				(require-not (message-number 711))
+				(require-not (message-number 904))
+				(require-not (message-number 206))
+				(require-not (message-number 800))
+				(require-not (message-number 712))
+				(require-not (message-number 207))
+				(require-not (message-number 718))
+				(require-not (state-flag "blastdoor-post-launch"))
+				(require-not (message-number 802))
+				(require-not (message-number 805))
+			)
+		)
+		(deny mach-message-send
+			(require-all
+				(message-number 805)
+				(require-not (message-number 804))
+				(require-not (state-flag "blastdoor-post-launch"))
+				(require-not (message-number 802))
+				(require-not (message-number 805))
+				(require-not (message-number 904))
+			)
+		)
+		(deny mach-message-send
+			(require-all
+				(message-number 904)
+				(require-not (message-number 804))
+				(require-not (message-number 805))
+				(require-not (message-number 803))
+				(require-not (message-number 711))
+				(require-not (state-flag "blastdoor-post-launch"))
+				(require-not (message-number 802))
+				(require-not (message-number 805))
+				(require-not (message-number 904))
+			)
+		)
+		(deny mach-message-send
+			(require-all
+				(state-flag "blastdoor-post-launch")
+				(require-not (message-number 804))
+				(require-not (message-number 805))
+				(require-not (message-number 803))
+				(require-not (message-number 711))
+				(require-not (message-number 904))
+				(require-not (message-number 206))
+				(require-not (message-number 800))
+				(require-not (message-number 712))
+				(require-not (message-number 207))
+				(require-not (message-number 718))
+			)
+		)
+		(deny mach-message-send
+			(require-all
+				(require-not (message-number 804))
+				(require-not (message-number 805))
+				(require-not (message-number 803))
+				(require-not (message-number 711))
+				(require-not (message-number 904))
+				(require-not (message-number 206))
+				(require-not (message-number 800))
+				(require-not (message-number 712))
+				(require-not (message-number 207))
+				(require-not (message-number 718))
+				(require-not (state-flag "blastdoor-post-launch"))
+				(require-not (message-number 802))
+				(require-not (message-number 805))
+				(require-not (message-number 904))
+			)
+		)
+	)
+)
+
 (allow mach-derive-port)
 
 (allow mach-lookup
```
