package entities.bullets;

import entities.Entity;
import entities.zombies.Zombie;
import managers.GamePlayer;
import java.awt.*;

/**
 * Generally represents the bullets of the game
 */
public class Bullet extends Entity {

    int destructionPower;
    int movingSpeed;

    /**
     * Instantialtes this class
     * @param xLocation The initial x location
     * @param yLocation The initial y location
     * @param destructionPower This bullets power
     * @param gamePlayer The owning game player
     */
    public Bullet(int xLocation, int yLocation, int destructionPower, GamePlayer gamePlayer) {
        super(10, xLocation, yLocation, 28, 28, gamePlayer);
        movingSpeed = 20;
        this.destructionPower = destructionPower;
    }

    @Override
    public void initialise(GamePlayer gamePlayer) {
        super.initialise(gamePlayer);
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
    public int getXLocation() {
        return super.getXLocation();
    }

    @Override
    public int getYLocation() {
        return super.getYLocation();
    }

    @Override
    public Image getAppearance() {
        return super.getAppearance();
    }

    /**
     * Hits and reduces the life of its opponent zombie
     * @param zombie The zombie this bullet bumps into
     */
    public void hit(Zombie zombie) {
        zombie.injure(destructionPower);
        life = 0;
        die();
    }

    /**
     * Moves this bullet along
     */
    public void move() {
        try {
            Thread.sleep(80);
            xLocation += movingSpeed;
            if (xLocation > 1300) {
                life = 0;
                die();
            }
        } catch (InterruptedException ignore) { }
    }

    @Override
    public void die() {
        super.die();
    }

    @Override
    public void run() {
        while (gamePlayer.isNotGameFinished() && life > 0) {
            if(gamePlayer.isGamePaused()) {
                try {
                    Thread.sleep(500);
                } catch (InterruptedException ignore) { }
            } else {
                gamePlayer.bumpBullet(this);
                move();
            }
        }
    }
}
