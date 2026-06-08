## MobileSoftwareUpdateXCTests.plist

> `Domain/MobileSoftwareUpdateXCTests.plist`

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>BATSConfigVersion</key>
	<string>0.1.0</string>
	<key>Project</key>
	<string>MobileSoftwareUpdate</string>
	<key>Tests</key>
	<array>
		<dict>
			<key>Arch</key>
			<string>platform-native</string>
			<key>AsRoot</key>
			<true/>
			<key>Command</key>
			<array>
				<string>BATS_XCTEST_CMD</string>
				<string>-NSTreatUnknownArgumentsAsOpen NO</string>
				<string>-ApplePersistenceIgnoreState YES</string>
				<string>-XCTest</string>
				<string>BrainTrustTests</string>
				<string>BrainTrustTests.xctest</string>
			</array>
			<key>ShowSubtestResults</key>
			<true/>
			<key>Tags</key>
			<array/>
			<key>TestName</key>
			<string>BrainTrustTests</string>
			<key>WorkingDirectory</key>
			<string>/AppleInternal/XCTests/com.apple.MobileSoftwareUpdate</string>
		</dict>
	</array>
	<key>Timeout</key>
	<real>3600.0</real>
</dict>
</plist>

```
