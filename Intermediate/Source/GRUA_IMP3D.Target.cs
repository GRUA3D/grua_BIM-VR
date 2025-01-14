using UnrealBuildTool;

public class GRUA_IMP3DTarget : TargetRules
{
	public GRUA_IMP3DTarget(TargetInfo Target) : base(Target)
	{
		DefaultBuildSettings = BuildSettingsVersion.V3;
		IncludeOrderVersion = EngineIncludeOrderVersion.Latest;
		Type = TargetType.Game;
		ExtraModuleNames.Add("GRUA_IMP3D");
	}
}
