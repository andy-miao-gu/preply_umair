package cards;

import enums.GameDifficulty;
import javax.swing.*;
import java.awt.*;

/**
 * Represents the card for the galting-pea shooter
 */
public class GaltingPeaShooterCard extends Card {

    private final int rechargeTime;
    private static GaltingPeaShooterCard galtingPeaShooterCard = null;

    /**
     * Instantiates this class
     * @param gameDifficulty The difficulty of the game, affecting the recharge time
     * @param xLocation The fixed x position of this card
     * @param yLocation The fixed y position of this card
     */
    private GaltingPeaShooterCard(GameDifficulty gameDifficulty, int xLocation, int yLocation) {
        super(new ImageIcon("Game accessories\\images\\Cards\\GaltingShooterCard.png").getImage(),
                xLocation, yLocation, 200);
        if(gameDifficulty == GameDifficulty.HARD)
            rechargeTime = 45000;
        else rechargeTime = 30000;
    }

    /**
     * This is a singleton model
     * @param gameDifficulty The difficulty of the game
     * @param xLocation The fixed x position of this card
     * @param yLocation The fixed y position of this card
     * @return The only object of this class
     */
    public static GaltingPeaShooterCard getInstance(GameDifficulty gameDifficulty, int xLocation, int yLocation) {
        if(galtingPeaShooterCard == null)
            galtingPeaShooterCard = new GaltingPeaShooterCard(gameDifficulty, xLocation, yLocation);
        return galtingPeaShooterCard;
    }

    @Override
    public void setEnabled(boolean enabled) {
        super.setEnabled(enabled);
    }

    @Override
    public void setCardImage(Image cardImage) {
        super.setCardImage(cardImage);
    }

    @Override
    public Image getCardImage() {
        return super.getCardImage();
    }

    @Override
    public int getXLocation() {
        return super.getXLocation();
    }

    @Override
    public int getYLocation() {
        return super.getYLocation();
    }

    @Override
    public int getRequiredEnergy() {
        return super.getRequiredEnergy();
    }

    @Override
    public int getWidth() {
        return super.getWidth();
    }

    @Override
    public int getHeight() {
        return super.getHeight();
    }

    @Override
    public boolean getEnabled() {
        return super.getEnabled();
    }

    @Override
    public void use() {
        setCardImage(new ImageIcon("Game accessories\\images\\Cards\\GaltingShooterCard-used.png").getImage());
        setEnabled(false);
        try {
            Thread.sleep(rechargeTime);
        } catch (InterruptedException ignore) { }
        setCardImage(new ImageIcon("Game accessories\\images\\Cards\\GaltingShooterCard.png").getImage());
        setEnabled(true);
    }

    @Override
    public void run() {
        use();
    }
}
